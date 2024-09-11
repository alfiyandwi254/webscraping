from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = '/path/to/chromedriver'

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to Hacker News
driver.get("https://www.topendsports.com/events/summer/hosts/list.htm")

# Retrieve the page source
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all 'tr' elements with class 'athing' which contain the news titles
titles = soup.find_all('tr')

# Loop through each title and print it
for title in titles:
    # Find the <a> tag within the 'titleline' span inside a 'td' with class 'title'
    title_link = title.find('td').text  # Extract the text of the title
    print(title_link)
    
# Close the driver
driver.quit()