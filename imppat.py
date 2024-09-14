import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def scrape_imppat(search_query):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://cb.imsc.res.in/imppat/basicsearch/phytochemical")

    data = []

    try:
        time.sleep(5)  # Allow the page to load

        # Find the search box and input the search query
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input#edit-combine.form-control"))
        )
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # Allow time for the results to load
        time.sleep(5)

        page_number = 1
        while True:
            print(f"Scraping page {page_number}...")

            # Extract table rows
            table_rows = driver.find_elements(By.CSS_SELECTOR, "table.table tr")

            # Iterate over the rows and extract the data (skip header row)
            for row in table_rows[1:]:
                columns = row.find_elements(By.TAG_NAME, "td")
                row_data = [col.text for col in columns]
                data.append(row_data)

            # Check if the "Next" button is disabled (no more pages to scrape)
            try:
                next_button = driver.find_element(By.LINK_TEXT, 'Next')
                # Check if the 'Next' button is disabled
                if 'disabled' in next_button.get_attribute('class'):
                    print(f"No more pages after page {page_number}. Ending scraping.")
                    break
                next_button.click()

                # Allow time for the next page to load
                time.sleep(5)
                page_number += 1
            except:
                print(f"No 'Next' button found or no more pages after page {page_number}. Ending scraping.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

    return data

def save_to_csv(data, filename):
    if data:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header dynamically based on the first row
            header = ["Column " + str(i+1) for i in range(len(data[0]))]
            writer.writerow(header)  # Header
            for row in data:
                writer.writerow(row)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

def main():
    search_query = "Curcuma longa"  # You can change this to search for different plants
    filename = "imppat_data.csv"

    # Scrape data
    data = scrape_imppat(search_query)

    # Save data to CSV
    save_to_csv(data, filename)

if __name__ == "__main__":
    main()

