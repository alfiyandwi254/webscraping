# from this -->
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
# to this --> it's like basic format library for selenium that'll used for scrapping
# the pandas is used for convert your scraped data to dataframe & Keys is used to hit keys like enter, shift, etc.

# first we initialize the path/url where contain the data that we want to scrape
path = 'https://opentrolley.co.id/'

# make sure to specify the path to your chromedriver in service
# in some source that i've been read, you can write like this or you can add 'executable_path', it's up to you
service = Service('C:/Users/operation.support/Documents/web scrap/chromedriver-win64/chromedriver.exe')  

# initialize the webdriver with the service that we have been add
driver = webdriver.Chrome(service=service)

# and this for launch the web from path/URL
driver.get(path)

# this is the condition if you want to make sure that web will wait until found the content/element you are searching for
# the library that used here are WebDriverWait and and expected_conditions or alias 'EC'
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "w3-row")]')))

# here i want to search for element-element where contain the data that I want to scrape
# you can open the web, right click and click inspect
# there you can see that the catalog is store on XPATH '//div[contains(@class, "w3-row")]'
# this the format for initialize the XPATH
# -> slash (//) is the format
# -> div = the tag of HTML, or you can search for all tag by add * or maybe like this (//*[contains(@class, "w3-row")])
# -> contains = is function to add conditions, if we read it was like "if the class have 'w3-row' in it" something like that
catalogs = driver.find_element(By.XPATH, '//div[contains(@class, "w3-row")]')

# then we search where is the information of every single product, it was ini class = 'detail'
catalogy = catalogs.find_elements(By.XPATH, '//div[contains(@class, "detail")]')

# we initialize the empty array to store our data
catalogList = []

# and after we initialize the body (catalogy), we use it for looping like this
for catalog in catalogy:
    # inside the body contain the data that we want to get
    # in my case, I want to get the title, description, and the link for go to the product in every category
    title = catalog.find_element(By.CLASS_NAME, 'title').text
    description = catalog.find_element(By.CLASS_NAME, 'desc').text
    
    # to get the information about link/href, if we see the HTML, the href is inside 'a' tag, so we can search it by tag name
    link = catalog.find_element(By.TAG_NAME, 'a').get_attribute('href')
    
    # then we append/store the data to catalogList that we have been declared before
    catalogList.append([title, description, link])

# we can check the catalogList
# print(catalogList)

# and for the last we convert the catalogList to dataframe
df = pd.DataFrame(catalogList, columns=['Title', 'Description', 'Link'])
# and export it to excel, you can export it to csv by change the function 'to_excel' --> 'to_csv'
# df.to_excel('catalogue.xlsx', index=False)
# print(catalogList)


nextPage = [link[2] for link in catalogList]
descNext = []

# for i in range(int(len(nextPage))):
urlNext = nextPage[0]
driver.get(urlNext)

wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "search-results-content")]')))    
result = driver.find_element(By.CLASS_NAME, 'search-results-content')
resultContent = result.find_elements(By.XPATH, '//div[contains(@class, "w3-row")]')
print(len(resultContent))
# for content in resultContent:

    # detail = content.find_element(By.XPATH, '//div[contains(@class, "book-title")]')
    # title1 = detail.find_element(By.XPATH, '//a[contains(@id, "aTitle")]').text
    # detailAuth = content.find_element(By.XPATH, '//div[contains(@class, "book-author")]')
    # author = detailAuth.find_element(By.XPATH, '//a[contains(@id, "aAuthorURL1")]').text
    # status = content.find_element(By.XPATH, '//div[contains(@class, "stock-status")]').text
    # normalPrice = content.find_element(By.XPATH, '//span[contains(@id, "NormalPrice")]').text
    # discountPrice = content.find_element(By.XPATH, '//span[contains(@id, "lblPrice")]').text
    
    # descNext.append([title1, author, status, normalPrice, discountPrice])
        
# print(descNext)

# contentDf = pd.DataFrame(descNext, columns=['Title', 'Author', 'Status', 'Normal Price', 'Discount Price'])
# print(contentDf)

# close the driver
driver.quit()