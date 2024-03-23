from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://watchmanprivacy.libsyn.com/')

driver.implicitly_wait(5)

ids = driver.find_elements(by=By.XPATH, value='//*[@id]')
for ii in ids:
    #print ii.tag_name
    print(ii.get_attribute('id'))

# get all the embed ids, scrolling down the page
# infinite scroll... shout out to the below link
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# for each embed id, grab the source and strip the html://// from the beginning

## open the source in a new window

## click the download button, close the window
