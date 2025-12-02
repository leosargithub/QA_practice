#import webdriver module
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#instantiate webdriver and launch chrome browsers

browser = webdriver.Chrome()
browser.maximize_window()

#open url
browser.get("https://dmytro-ch21.github.io/html/web-elements.html")
title = browser.title
print(f"window {title}")

#fetch url and print
print("url:", browser.current_url)

#
# #find check box and select checkbox
# checkbox_ford = browser.find_element(By.ID, "option1")
#
# if not checkbox_ford.is_selected():
#     checkbox_ford.click()
#
# checkbox_bmw = browser.find_element(By.ID, "option2")
# checkbox_bmw.click()
#
# checkbox_mercedes= browser.find_element(By.ID, "option3")
# checkbox_mercedes.click()
#
# #veryfy selection
# print("is Ford selected ", checkbox_bmw.is_selected())
# print("is Mercedes selected", checkbox_mercedes.is_selected())

# find elements and check multiple checkboxes
checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()

time.sleep(5)
browser.quit()