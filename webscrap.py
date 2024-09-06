import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"

services = Service(executable_path=browser_path)

# Initialize the Chrome WebDriver with the Service object
driver = webdriver.Chrome(service=services)

url = ("https://www.pajak.go.id/id/daftar-pejabat-page")

# Open the webpage
driver.get(url)
# Optional: Wait for the page to fully load

time.sleep(5)

# Initialize a list to store the scraped data
data_list = []

# Locate elements (modify selectors based on the webpage structure)
elements = driver.find_elements(By.CLASS_NAME, 'desired-class-name')

# Extract text from each element and append to the list
for element in elements:
    data_list.append(element.text)

df = pd.DataFrame(data_list, columns=['Scraped Data'])
print(df)
# Save DataFrame to an Excel file
# df.to_excel('scraped_data.xlsx', index=False)

# Close the WebDriver
driver.quit()