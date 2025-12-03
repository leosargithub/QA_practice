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

multi_dropdown = Select(browser.find_element(By.ID, "multiSelect"))
multi_dropdown.select_by_index(0)
multi_dropdown.select_by_index(1)
multi_dropdown.select_by_index(2)
multi_dropdown.select_by_index(3)
time.sleep(2)
multi_dropdown.deselect_all()

if multi_dropdown.is_multiple:
    print("Dropdown is multiselect")
else:
    print("Dropdown is not multiselect")

selected_option = multi_dropdown.all_selected_options
for option in selected_option:
   print("All dropdown is select", option.text )

all_options = multi_dropdown.options
for option in all_options:
    print(option.text)
time.sleep(3)
browser.quit()