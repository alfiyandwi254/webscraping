import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.wpewebkit.webdriver
import pandas as pd
# from bs4 import BeautifulSoup

chrome_options = Options()
# chrome_options.add_argument("--headless")

# Initialize the Chrome WebDriver with the Service object
service = Service('C:/Users/operation.support/Documents/web scrap/chromedriver-win64/chromedriver.exe')  # Make sure to specify the path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

url = ("https://www.google.com")

# Open the webpage
driver.get(url)

driver.set_window_size(982, 655)

# Initialize a list to store the scraped data
data_list = []
wait = WebDriverWait(driver, 15)
search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))

# Locate elements (modify selectors based on the webpage structure)
elements = driver.find_element(By.CLASS_NAME, 'gLFyf')  # Adjust selector as needed
elements.send_keys("Iphone 15 Pro" + Keys.ENTER)

wait.until(EC.presence_of_element_located((By.ID, 'search')))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pnnext"))).click()

# Locate result items
google = driver.find_elements(By.CLASS_NAME, 'CA5RN')

df ={}

page = driver.find_element(By.CLASS_NAME, 'AaVjTc')
pages = driver.find_element(By.CLASS_NAME, 'Nj8Yyf')
nextPage = page.find_elements(By.CLASS_NAME, 'fl')
nextPage2 = page.find_element(By.CLASS_NAME, 'wABy2b z1asCe GNeCNe') 
# acRNod IpLO9 IEQr4b

google2 = driver.find_elements(By.CLASS_NAME, 'wbJOMb')

n = 10
# nextp = driver.find_element(By.ID, "pnnext")
for j in range(1,n,1):
    for item in google:
        if j == 1:
            wait
            groo = item.find_element(By.CLASS_NAME, 'VuuXrf').text
            valueh = item.find_element(By.CLASS_NAME, 'byrV5b').text
            if groo != '' and groo not in df:
                df[groo] = valueh
            nextPage[j].click()
        elif j != 1:
            wait    
            groo = item.find_element(By.CLASS_NAME, 'OSrXXb').text
            valueh = item.find_element(By.CLASS_NAME, 'OSrXXb VN4UC').text
            if groo != '' and groo not in df:
                df[groo] = valueh
            nextPage2.click()


print(df)

# Save DataFrame to an Excel file
# df.to_excel('scraped_data.xlsx', index=False)


    
# time.sleep(10)

# Close the WebDriver
driver.quit()