import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from undetected_chromedriver import Chrome, ChromeOptions

chrome_options = ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-gpu")
driver = Chrome(options=chrome_options)
driver.maximize_window()

#driver.execute_script("arguments[0].scrollIntoView();", all_listings[-1])
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")            

driver.get('')

driver.find_element(By.XPATH, '').click()