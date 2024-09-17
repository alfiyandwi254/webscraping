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
chrome_options.add_argument("--headless")

# Initialize the Chrome WebDriver with the Service object
service = Service('C:/Users/operation.support/Documents/web scrap/chromedriver-win64/chromedriver.exe')  # Make sure to specify the path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

url = ("https://en.wikipedia.org/wiki/List_of_Game_of_the_Year_awards")

# Open the webpage
driver.get(url)

driver.set_window_size(982, 655)

# Initialize a list to store the scraped data
data_list = []

# Initialize WebDriverWait, so the driver can waiting until found the content we search for
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located(By.CLASS_NAME, 'mw-page-container'))

# Locate elements (modify selectors based on the webpage structure)
elements = driver.find_element(By.CLASS_NAME, 'mw-page-container')  # Adjust selector as needed

# Locate result items
#Initialize the location of table
table = driver.find_element(By.CLASS_NAME, 'wikitable')

#Initialize the location for row table, that'll be used for looping
rows = table.find_elements(By.TAG_NAME, 'tr')

for row in rows:
    cols = row.find_elements(By.TAG_NAME, 'td')
    # Convert WebElement text to a list of strings
    data_row = [col.text for col in cols]
    
    # Handle specific cases if needed
    if len(cols) == 3:
        data_row.insert(0, '8888')  # Insert as string, not integer
    elif len(cols) == 0:
        continue  # Skip empty rows

    data_list.append(data_row)
# Convert the list to a DataFrame
df =[]
df = pd.DataFrame(data_list)
print(df)

# Save DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)

time.sleep(10)

# Close the WebDriver
driver.quit()