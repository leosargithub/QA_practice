
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# to handle drop-down menu import select module
import selenium.webdriver.support.ui
from selenium.webdriver.support.select import Select

#instantiate webdriver and launch chrome browsers

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://uitestingplayground.com/alerts")

# alert_btn =  browser.find_element(By.ID, "alertButton")
# alert_btn.click()
# time.sleep(4)
# # switch focus to alert popup
# alert = browser.switch_to.alert
# print("alert message: ", alert.text)
# alert.accept()

# confirmation_btn = browser.find_element(By.ID,"confirmButton")
# confirmation_btn.click()
# time.sleep(3)
#
#
# alert = browser.switch_to.alert
# print("alert message: ", alert.text)
# alert.dismiss()
# time.sleep(2)
# simple_alert = browser.switch_to.alert
# print("alert message: ", simple_alert.text)
# simple_alert.accept()


prompt_alert = browser.find_element(By.ID, "promptButton")
prompt_alert.click()
time.sleep(3)

alert = browser.switch_to.alert
print("alert message", alert.text)


time.sleep(2)
alert.send_keys("hello bor")
time.sleep(2)

simple_alert = browser.switch_to.alert
print("simple alert", simple_alert.text)

simple_alert.accept()



time.sleep(3)
browser.quit()
