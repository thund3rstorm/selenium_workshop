from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def setup():

	driver_path="/usr/lib/chromium-browser/chromedriver"
	return webdriver.Chrome(driver_path)

#search
def search(browser,search_term):
	searchbox = browser.find_element_by_id("searchBox")
	
	searchbox.send_keys(Keys.CONTROL,'a')
	searchbox.send_keys(Keys.DELETE)


	searchbox.send_keys(search_term)

	#add on click button
	searchbtn = browser.find_element_by_id("basic-addon2")
	searchbtn.click()


browser=setup()
browser.get("https://demoqa.com/books")

#manually entering search terms
"""
while True:
	user_ip = input("search y/n")
	if user_ip == "y":
		search_term=input("Enter the search_term")
		search(browser,search_term)
		time.sleep(2)
	elif user_ip == "n":
		break
"""
# Iterating search terms from a list

search_terms = ["python","javascript","c"]
for search_term in search_terms:
    search(browser,search_term)
    time.sleep(2)

browser.close()