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

verdict_li = []

df = pd.read_csv('varun_pdfurl.csv')
for index, row in df.iterrows():
    
    name = row['Name']

    n = name.split('Ltd')[0].strip()

    try:
        driver.get('https://www.chittorgarh.com/search.asp')
        
        time.sleep(random.randint(3,6))
        
        driver.execute_script("window.scrollTo(0, 0);")
        searchbox = driver.find_element(By.XPATH, '//input[@class="gsc-input"]')
        searchbox.send_keys(n)

        driver.find_element(By.XPATH, '//*[@class="gsc-search-button"]').click()

        time.sleep(random.randint(3,6))

        url = driver.find_element(By.XPATH, '//*[@class="gs-title"]/a').get_attribute('href')

        driver.get(url)

        time.sleep(random.randint(3,6))

        #driver.find_element(By.XPATH, '//*[@title="IPO Reviews & Recommendation"]').click()

        verdict = driver.find_element(By.XPATH, '//*[@id="main"]/div[9]/div/h2').text
        
        print(n,":",verdict)
        verdict_li.append(verdict)

    except:

        input('debug')

df["Chittorgarh"] = verdict_li
df.to_csv('varun_with_chittorgarh.csv')