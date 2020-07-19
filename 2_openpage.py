from selenium import webdriver
import time

#path of  the driver
driver_path="/usr/lib/chromium-browser/chromedriver"

#start the session
browser = webdriver.Chrome(driver_path)

#open a page in browser window
browser.get("https://codersarena.now.sh/")
time.sleep(3)
browser.get("https://www.google.com")

#wait for the user
input()
browser.close()