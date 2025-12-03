
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
browser.get("https://dmytro-ch21.github.io/html/web-elements.html")
# title = browser.title
# print(f"window {title}")
#
# #fetch url and print
# print("url:", browser.current_url)

# find custom dropdown
search_dropdown = browser.find_element(By.CLASS_NAME, "search-box")
# use javascript to scroll the web page to make dropdown visible
browser.execute_script("arguments[0].scrollIntoView(true);", search_dropdown)
time.sleep(3)
search_dropdown.click()

#  enter text 'S'
search_dropdown.send_keys('S')

time.sleep(5)
# fin suv option from dropdown
option = browser.find_element(By.XPATH, "//div[@class='searchable-option' and text()='SUV']")
option.click()
# find custom dropdown web element

time.sleep(4)
browser.quit()