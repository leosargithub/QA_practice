#import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.maximize_window()

browser.get("https://practice.expandtesting.com/")




test_login = browser.find_element(By.LINK_TEXT, "Test Login Page")

# scroll
browser.execute_script("arguments[0].scrollIntoView(true);",test_login)

test_login.click()






time.sleep(3)
browser.quit()