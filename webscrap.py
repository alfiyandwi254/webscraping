import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
# from bs4 import BeautifulSoup

chrome_options = Options()
# chrome_options.add_argument("--headless")

# Initialize the Chrome WebDriver with the Service object
# driver = webdriver.Chrome()

service = Service('C:/Users/operation.support/Documents/web scrap/chromedriver-win64/chromedriver.exe')  # Make sure to specify the path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

url = ("https://www.google.com")

# Open the webpage
driver.get(url)

# Initialize a list to store the scraped data
data_list = []
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
# Locate elements (modify selectors based on the webpage structure)
elements = driver.find_element(By.CLASS_NAME, 'gLFyf')  # Adjust selector as needed
elements.send_keys("Iphone 15 Pro" + Keys.ENTER)

wait.until(EC.presence_of_element_located((By.ID, 'search')))

# Locate result items
items = driver.find_elements(By.CLASS_NAME, 'wbJOMb')

# items = driver.find_elements(By.CLASS_NAME, 'Aozhyc Sqrs4e TElO2c OSrXXb')
for item in items:
    groo = item.find_element(By.CLASS_NAME, 'OSrXXb')
    df = df.append({'Title': item.text}, ignore_index=True)
print(df)
# Save DataFrame to an Excel file
# df.to_excel('scraped_data.xlsx', index=False)

# time.sleep(10)

# Close the WebDriver
driver.quit()