from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

path = 'https://opentrolley.co.id/'
service = Service('C:/Users/operation.support/Documents/web scrap/chromedriver-win64/chromedriver.exe')  # Make sure to specify the path to your chromedriver
driver = webdriver.Chrome(service=service)

driver.get(path)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "w3-row")]')))

catalogs = driver.find_element(By.XPATH, '//div[contains(@class, "w3-row")]')
catalogy = catalogs.find_elements(By.XPATH, '//div[contains(@class, "detail")]')
# books = catalogs.find_elements(By.CLASS_NAME, 'search-results-content')
catalogList = []
i=0
for catalog in catalogy:
    title = catalog.find_element(By.CLASS_NAME, 'title').text
    description = catalog.find_element(By.CLASS_NAME, 'desc').text
    # links = catalog.find_element(By.XPATH, '//div[contains(@class, "more")]')
    link = catalog.find_element(By.TAG_NAME, 'a').get_attribute('href')
    catalogList.append([title, description, link])
    

# for book in books:
#     wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@id, "homefindoutmore")]')))
#     findMore = book.find_element(By.XPATH, '//div[contains(@id, "homefindoutmore")]')
#     findMore.click()


print(catalogList)
df = pd.DataFrame(catalogList, columns=['Title', 'Description', 'Link'])
df.to_excel('catalogue.xlsx', index=False)
