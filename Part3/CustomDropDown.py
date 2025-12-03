
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
dropdown = browser.find_element(By.ID, "custom-select")
# use javascript to scroll the web page to make dropdown visible
browser.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(3)
dropdown.click()


# find custom dropdown web element
custom_dropdown = browser.find_element(By.XPATH, "//div[@class='custom-options']/div[text()='Red']")
custom_dropdown.click()

dropdown = browser.find_element(By.ID, "custom-select")
# use javascript to scroll the web page to make dropdown visible
browser.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(3)
dropdown.click()
custom_dropdown_blue = browser.find_element(By.XPATH, "//div[@class='custom-options']/div[text()='Blue']")
custom_dropdown_blue.click()
time.sleep(4)
browser.quit()