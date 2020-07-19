from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def setup():

	driver_path="/usr/lib/chromium-browser/chromedriver"
	return webdriver.Chrome(driver_path)

def goto_home(browser):
	full_home_xpath = "/html/body/header/div/nav/ul/li[1]/a"
	half_home_xpath = '//*[@id="header"]/div/nav/ul/li[1]/a'
	home = browser.find_element_by_xpath(full_home_xpath)
	home.click()

def goto_aboutus(browser):
	aboutus_xpath= '//*[@id="header"]/div/nav/ul/li[2]/a'
	aboutus = browser.find_element_by_xpath(aboutus_xpath)
	aboutus.click()

def goto_courses(browser):
	courses_xpath= '//*[@id="header"]/div/nav/ul/li[3]/a'
	courses = browser.find_element_by_xpath(courses_xpath)
	courses.click()


def goto_contact(browser):
	contact_xpath= '//*[@id="header"]/div/nav/ul/li[4]/a'
	contact = browser.find_element_by_xpath(contact_xpath)
	contact.click()


browser=setup()


browser.get("https://codersarena.now.sh")


for i in range(10):
	goto_home(browser)
	goto_aboutus(browser)
	goto_courses(browser)
	goto_contact(browser)

	print(i)