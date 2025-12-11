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
browser.get("https://dmytro-ch21.github.io/html/web-elements.html")
title = browser.title
print(f"window {title}")

#fetch url and print
print("url:", browser.current_url)

# locate the single-select dropdown
# dropdown = Select( browser.find_element(By.ID, "carBrands"))
# dropdown.select_by_index(1)
#
# dropdown = Select( browser.find_element(By.ID, "carBrands"))
# dropdown.select_by_value("mercedes")
#
# dropdown = Select( browser.find_element(By.ID, "carBrands"))
# dropdown.select_by_visible_text("Volvo")

# dropdown = Select( browser.find_element(By.ID, "carBrands"))
# print("Selected option", dropdown.first_selected_option.text)

#check if dropdown is multiselect

dropdown = Select( browser.find_element(By.ID, "carBrands"))
if dropdown.is_multiple:
    print("This dropdown is multiselect")
else:
    print("This dropdown is not multiselected ")

time.sleep(5)

browser.quit()