#import webdriver module
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# to handle drop-down menu import select module
import selenium.webdriver.support.ui
from selenium.webdriver.support.select import Select

#instantiate webdriver and launch chrome browsers

browser = webdriver.Chrome()
browser.maximize_window()

#open url
browser.get("https://www.google.com")
title = browser.title
print(f"window {title}")

#fetch url and print
print("url:", browser.current_url)

search = browser.find_element(By.ID, "APjFqb")
search.send_keys('Quality Assurance')

time.sleep(4)

suggestion = browser.find_elements(By.XPATH, "//ul[@role='listbox']/li ")

for suggestion_search in suggestion:
    print(suggestion_search.text)



browser.quit()