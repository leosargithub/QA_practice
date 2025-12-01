from selenium import  webdriver
import time
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.saucedemo.com")

time.sleep(2)

#locate username web element
username = browser.find_element(By.NAME, "user-name")


#enter username
username.send_keys("standard_user")

time.sleep(2)

password = browser.find_element(By.NAME, "password")


#enter password
password.send_keys("secret_sauce")


#button click
loginBtn = browser.find_element(By.NAME, "login-button")
loginBtn.click()
time.sleep(2)


#close browser
browser.quit()
