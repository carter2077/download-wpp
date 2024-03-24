from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://watchmanprivacy.libsyn.com/')

# let the page load
driver.implicitly_wait(5)

# scroll all the way down the page so we can get all embeds
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

# get all embeds
embeds = driver.find_elements(by=By.CSS_SELECTOR, value="[id^=embed_]")

# for each embed id, grab the source and strip the html://// from the beginning
original_window = driver.current_window_handle
for e in embeds:
    url = e.get_attribute("src")
    # open the source in a new tab
    driver.switch_to.new_window('tab')
    print("Downloading {}...".format(url))
    driver.get(url)
    # click the download button, close the window
    # probably not waiting the correct way here
    driver.implicitly_wait(0.5)
    dl_btn = driver.find_element(by=By.ID, value="download-player")
    dl_btn.click()
    driver.implicitly_wait(1)
    driver.close()
    driver.implicitly_wait(0.5)
    driver.switch_to.window(original_window)
    driver.implicitly_wait(0.5)

