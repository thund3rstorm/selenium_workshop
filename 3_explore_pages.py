from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#path of  the driver
driver_path="/usr/lib/chromium-browser/chromedriver"

#start the session
browser = webdriver.Chrome(driver_path)

#open a page in browser window

landing_page = browser.get("https://www.google.com/")

search_bar = browser.find_element_by_name("q")
search_bar.send_keys("Google")
#click on search button
#search_button = browser.find_element_by_name("btnK")
search_bar.send_keys(Keys.ENTER)


input()
browser.close()