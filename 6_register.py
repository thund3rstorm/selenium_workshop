from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
# setup browser
def setup():
    driver_path="/usr/lib/chromium-browser/chromedriver"
    return webdriver.Chrome(driver_path)
 
 
def register(browsaer,user):
    browser.get("https://demoqa.com/register")
 
    # Elements
    first_name = browser.find_element_by_id("firstname")
    last_name = browser.find_element_by_id("lastname")
    user_name = browser.find_element_by_id("userName")
    password = browser.find_element_by_id("password")
    register = browser.find_element_by_id("register")
    # Send Keys
    first_name.send_keys(user['first_name'])
    last_name.send_keys(user['last_name'])
    user_name.send_keys(user['user_name'])
    password.send_keys(user['password'])
    # wait for human
    input("Solve Captcha")
    time.sleep(2)
    # Click on register
    register.click()
 
def login(browser,user):
    #elements
    browser.get("https://demoqa.com/login")
    user_name = browser.find_element_by_id("userName")
    password = browser.find_element_by_id("password")
    login = browser.find_element_by_id("login")
    
    #send keys
    user_name.send_keys(user['user_name'])
    password.send_keys(user['password'])

    time.sleep(2)
    #click on login
    login.click()

 
# ////////// MAIN
 
browser = setup()
# User Object
user = {
    "first_name" : "Tony",
    "last_name" : "Stark",
    "user_name" : "ironman123",
    "password"  : "Stark@3000"
}
register(browser,user)
login(browser,user)
