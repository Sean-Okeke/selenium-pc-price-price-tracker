import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os
import re


#Converts so it's easier to compare prices
def extract_price_number(price_text):
    numbers = re.sub(r"[^\d]", "", price_text)
    if numbers:
        return int(numbers)
    return None


#Opens website and gets price
def scrape_product(driver, product):
    name = product["name"]
    url = product["url"]
    css_selector = product["selector"]
    target_price = product["target_price"]
    print(f"\nChecking {name}...")

    try:
        #Open webpage
        driver.get(url)

        # Wait up to 10 seconds for the element to actually load onto the screen
        wait = WebDriverWait(driver, 10)
        price_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        price_text = price_element.text
        print("Current Price:", price_text)
        price_number = extract_price_number(price_text)
        #Deal alert
        if target_price and price_number:
            if price_number <= target_price:
                print("🔥 DEAL FOUND!")
        return {
            "name": name,
            "price_text": price_text,
            "price_number": price_number,
            "url": url,
            "time": time.ctime()
            }
    except Exception as e:
        print("Error:", e)
        return None


#Loads previous history
def load_history(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []


#Saves updated history
def save_history(filename, history):
    with open(filename, "w") as file:
        json.dump(history, file, indent=4)


#Products to track
shopping_list = [
   {
       "name": "RTX 5080 (Micro Center)",
       "url": "https://www.microcenter.com/product/690482/pny-nvidia-geforce-rtx-5080-epic-x-rgb-overclocked-triple-fan-16gb-gddr7-pcie-50-graphics-card",
       "selector": "#options-pricing2022",
       "target_price": 1200
       },
    {
        "name": "RTX 5090 (Shop BLT)",
        "url": "https://www.shopblt.com/cgi-bin/shop/shop.cgi?action=thispage&thispage=011002501502_BYS0183P.shtml&order_id=!ORDERID!",
        "selector": "#yourprice",
        "target_price": 3500
        },
    {
        "name": "RTX 5080 (Ebay)",
        "url": "https://www.ebay.com/itm/336563563860?_skw=rtx+5080&epid=26075152229&itmmeta=01KQPJ2Y8FXB3XGTXHDHVB4ZJB&hash=item4e5cc06d54:g:GfcAAeSw6oxp9Vx5&itmprp=enc%3AAQALAAAA8GfYFPkwiKCW4ZNSs2u11xBU6dspKmUJw%2F31aHOfeFFvCKqWvkEtYZduPR%2BPvDNpmwmsKRehuUept1nJP%2FiHi2J2S9vd%2F7K2GOBMoes1PBjBeFO61jIqKZ3OXWA746WydEZDpclyjM1ZWX8N41P0OAtXZDBHMclSX7G6GWRsYeTlN%2Fp7w%2FfdDLkzDedbqITMPd%2BCupmNAc78xBoxweMi67ooYosxaeIgsn1q5PN7pfZTGwIHRAUiNsMt4ZrXWh8zsVciqvxEMk7SeiA3TpEJeBZS94bcGvwOdJ0ljFwJMPRZQjW1qlwAALmkZPntMXegbg%3D%3D%7Ctkp%3ABk9SR7Dki9K9Zw",
        "selector": "div.x-price-primary",
        "target_price": 1800
        },
    {
        "name": "Asus ROG Strix Scar 18 (Konga)",
        "url": "https://www.konga.com/product/asus-rog-strix-scar-18-intel-core-ultra-9-64gb-ram-4tb-ssd-18-display-nvidia-geforce-rtx-5090-black-6916435?cid=7796",
        "selector": "span.text-base.font-semibold.text-gray-900",
        "target_price": 10000000
        },
    {
        "name": "Samsung QD-OLED G9 Monitor (Jumia)",
        "url": "https://www.jumia.com.ng/samsung-odyssey-qd-oled-g9-49-curved-ultrawide-gaming-monitor-419558954.html",
        "selector": "span.-b.-fs24",
        "target_price": 3000000
        },
    {
        "name": "Palit RTX 5080 (Overclockers UK)",
        "url": "https://www.overclockers.co.uk/palit-geforce-rtx-5080-gaming-pro-16gb-gddr7-pci-express-graphics-card-gra-pal-04059.html",
        "selector": '[data-qa="price-current"]',
        "target_price": 110000
        },
    {
        "name": "RTX 5090 (Jiji)",
        "url": "https://jiji.ng/ikeja/computer-hardware/msi-geforce-rtx-5090-gaming-trio-oc-graphics-card-r3CuIAo3XpdZvnoUalXH92QR.html?page=1&pos=3&cur_pos=3&ads_per_page=16&ads_count=117&lid=NNQLV5UY_RlhW0yU&indexPosition=2",
        "selector": "span.qa-advert-price-view-value",
        "target_price": 6500000
        },
    {
        "name": "Seagate 2TB (Kara)",
        "url": "https://kara.com.ng/seagate-2tb-external-hard-drive",
        "selector": "p.text-2xl.font-semibold",
        "target_price": 135000
        },
    {
        "name": "Transcend 8GB RAM (Kusnap)",
        "url": "https://kusnap.com/product/2530662-8gb-pc-ram-card?productName=8gb+Pc+Ram+Card",
        "selector": "div.text-2xl.font-semibold.tracking-tight",
        "target_price": 20000
        }

   ]


#Browser setup
print("--- STARTING TRACKER ---")
options = uc.ChromeOptions()

#Remove this line if you want to watch the browser
#options.add_argument("--headless=new")

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)


#Main
history_file = "price_history.json"
history = load_history(history_file)
for item in shopping_list:
    result = scrape_product(driver, item)
    if result:
        history.append(result)
    time.sleep(3)
save_history(history_file, history)
driver.quit()
print("\n--- DONE ---")
