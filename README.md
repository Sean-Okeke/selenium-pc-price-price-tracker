# selenium-pc-price-price-tracker
A better version of my previous python automated web scraping tool, made using selenium and undetected-chromedriver designed to monitor prices of products across various local and international online shopping websites. This one is able to bypass bot protection and scrape prices for websites that make use JavaScript for rendering.

## Features
* **Multi-site dynamic scraping:** Able to pull data from multiple stores with varying html structures, including JavaScript rendered pages.
* **Anti-bot evasion:** Uses undetected-chromedriver and custom browser options to bypass advanced anti-automation protections.
* **Automated price extraction:** Uses regular expressions to clean and convert raw HTML price text into integers for accurate mathematical comparison.
* **Deal Alerts:** Compares live prices against custom target thresholds and flags the console when a product drops below the target price.
* **Data logging:** Automatically saves the scraped data with timestamps and URLs into a local price_history.json file for historical tracking.
* **Resilient design:** Includes explicit wait handling (WebDriverWait) and error catching to prevent the script from crashing if a site fails to load.

## Technologies Used
* Python 3.14.6
* `selenium` (Web browser automation framework)
* `undetected-chromedriver` (Anti-detection browser automation)
* `json`, `re`, `os`, `time` (Python Standard Libraries)

## How to run

### Get the code
1. Click on `Selenium_based_PC_Parts_Tracker.py` at the top of this page.
2. Click on the "Download raw file" button.

### Install dependencies
This script requires third party Python libraries. Open your terminal or command prompt and run:
1. pip install selenium
2. pip install undetected-chromedriver

Run the program using an IDE of your choosing.

### Adding components to track
1. In the `shopping_list` array, type in the name of the product.
2. Paste the URL of the product page.
3. Right click the price of the product on the site and click inspect element.
4. Enter the CSS `selector` for the price element.
5. Enter a `target_price` if you want to be alerted when the price falls below that.

*Note: This version directly upgrades my previous static scraper by utilizing `selenium` and `undetected-chromedriver`. This allows the program to render pages loading content through JavaScript and bypass modern bot-protection features that previously blocked standard HTTP requests. There is one small flaw, in line 133 removing the "#" in front of the comment enables `headless` mode which allows websites to be loaded in the background, but websites with advanced bot protection will be unable to load because they need to open a browser page to be able to bypass it, which is why I have chosen to keep `headless` mode off.*

## Author
**Sean Okeke**
* GitHub: [@Sean-Okeke](https://github.com/Sean-Okeke)
