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

#find radio button by id
radio_ford = browser.find_element(By.ID, "radio1")
radio_ford.click()

time.sleep(2)

radio_bmw = browser.find_element(By.ID, "radio2")

radio_bmw.click()



time.sleep(5)

browser.quit()