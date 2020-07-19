from selenium import webdriver

driver_path="drivers/chromedriver"
browser = webdriver.chrome(driver_path)
browser.close()