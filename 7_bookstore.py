from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
# setup browser
def setup():
    driver_path="/usr/lib/chromium-browser/chromedriver"
    return webdriver.Chrome(driver_path)

def textbox(browser,details):
	
	browser.maximize_window() #maximize browser window if some buttons generate "not clickable" error

	browser.get("https://demoqa.com/text-box")
	#elements
	fullname = browser.find_element_by_id("userName")
	email = browser.find_element_by_id("userEmail")
	current_address = browser.find_element_by_id("currentAddress")
	perm_address = browser.find_element_by_id("permanentAddress")
	submit_btn = browser.find_element_by_id("submit")

	fullname.send_keys(details['name'])
	email.send_keys(details['email'])
	current_address.send_keys(details['c_address'])
	perm_address.send_keys(details['p_address'])
	
	time.sleep(2)

	submit_btn.click()


#MAIN
browser = setup()
details = {
    "name" : "John Cena",
    "email" : "johncena@wwe.com",
    "c_address" : "Texas",
    "p_address"  : "New York"
}
textbox(browser,details)
