
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, csv

ele_list = []

# Set up chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

for page in range(1,3):
    url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=%7Bpage%7D'
    driver.get(url)
    time.sleep(2) # Optional wait to ensure page loads

    # Extract product details
    titles = driver.find_elements(By.CLASS_NAME, 'title')
    prices = driver.find_elements(By.CLASS_NAME, 'price')
    descriptions = driver.find_elements(By.CLASS_NAME, 'description')
    ratings = driver.find_elements(By.CLASS_NAME, 'ratings')

    # Store results in csv 
    with open('scrape.csv', 'a') as file:
        write = csv.DictWriter(file, fieldnames=['Title', 'Price', 'Description', 'Ratings'])
        #for i in range(len(titles)):
        write.writerows([{'Title': titles[i].text, 'Price': prices[i].text, 
                              'Description': descriptions[i].text, 
                              'Ratings': ratings[i].text} for i in range(len(titles))])
        
driver.quit()


#for row in ele_list:
#    print(row)


