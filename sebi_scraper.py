import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import pandas as pd

chrome_options = ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-gpu")
driver = Chrome(options=chrome_options)
driver.maximize_window()

#driver.execute_script("arguments[0].scrollIntoView();", all_listings[-1])
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")            

#driver.get('https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3&ssid=15&smid=11') # Red Herring Docs
driver.get('https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3&ssid=15&smid=78') # Other Docs

df = pd.read_csv('dataset_na.csv', encoding='latin1')

url_li = []

for i in df['Name']:
    n = i.split('Ltd')[0].strip()
    sbox = driver.find_element(By.XPATH, '//*[@id="search"]')
    sbox.clear()
    sbox.send_keys(n)

    time.sleep(random.randint(1,3))

    go = driver.find_element(By.XPATH, '//*[@class="go-search go_search"]')
    go.click()

    time.sleep(random.randint(2,4))

    try:
        url = driver.find_element(By.XPATH, '//*[@id="sample_1"]/tbody/tr/td[2]/a').get_attribute('href')
    except:
        url = 'NA'

    url_li.append(url)

    time.sleep(random.randint(1,2))

df['Prospectus'] = url_li

df.to_csv('dataset_prospectus_na_fixed.csv')