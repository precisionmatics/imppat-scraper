# IMPPAT Scraper

This Python script is designed to scrape phytochemical information from the IMPPAT (Indian Medicinal Plants Phytochemistry and Therapeutics) database. The script performs automated searching and retrieves data about phytochemicals, then saves the information to a CSV file for further analysis.

## Features

- Automates the search of phytochemicals using Selenium WebDriver.
- Handles pagination to scrape data across multiple pages.
- Saves extracted data to a CSV file.

## Requirements

- Python 3.x
- Selenium
- WebDriver Manager

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/imppat-scraper.git

   Navigate to the project directory:

bash

cd imppat-scraper

Install the required packages:

bash

    pip install selenium webdriver-manager

### Usage

### 1.Open the script file and set your search query.
 
        Modify the search_query variable in the main function to specify the phytochemical or plant you want to search for.

 ### 2.Run the script:

    python imppat_scraper.py

    The script will scrape data from the IMPPAT database and save it to a CSV file named imppat_data.csv in the same directory.

### Example

To search for the phytochemical information of "Curcuma longa":

    Set search_query = "Curcuma longa" in the main function.
    Run the script as described above.
    Check imppat_data.csv for the extracted data.

## Contributing

Feel free to submit issues or pull requests. If you have suggestions or improvements, your contributions are welcome!

## license

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

    Selenium WebDriver
    WebDriver Manager
