
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# to handle drop-down menu import select module
import selenium.webdriver.support.ui
from selenium.webdriver.support.select import Select

#instantiate webdriver and launch chrome browsers

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://demo.guru99.com/V4/index.php")

loginBtn = browser.find_element(By.NAME, "btnLogin")
loginBtn.click()

time.sleep(4)



alert = browser.switch_to.alert  # switch focus to alert window
print("Alert message:", alert.text)
alert.accept()
time.sleep(3)
browser.quit()



