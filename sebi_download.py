import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import pandas as pd
import os

#driver.execute_script("arguments[0].scrollIntoView();", all_listings[-1])
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")            

df = pd.read_csv('dataset_prospectus.csv')

chrome_options = ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-gpu")

driver = Chrome(options=chrome_options)
driver.maximize_window()

url_li = []

for index, row in df.iterrows():  
    prospectus = row['Prospectus']
    name = row['Name']
    print(name)
    try:
        if 'sebi' in prospectus:
            driver.get(prospectus)
            time.sleep(random.randint(3,6))

            sbox = driver.find_element(By.XPATH, '//*[@class="cover"]/iframe')
            url_li.append(sbox.get_attribute('src').split('=')[1])
        else:
            url_li.append(prospectus)
    except:
        url_li.append('NA')

df['PDF URL'] = url_li
df.to_csv("datasetprospectus_pdfurl.csv")