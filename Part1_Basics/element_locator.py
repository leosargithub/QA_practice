from selenium import  webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.saucedemo.com")

time.sleep(5)