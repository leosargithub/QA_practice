from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

from Part10.BrowserAutomation import expected_url, expected_title

# launch browser & maximize window
browser = webdriver.Chrome()
browser.maximize_window()

# open url
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)

# get the unique ID of the currently active browser window
parent_window_id = browser.current_window_handle
print("Parent window id:", parent_window_id)

# find link Orange, Inc
browser.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()


# get all windows (IDs) after new windows is opened
list_window_ids = browser.window_handles

# print all windows id
print("All windows : ", list_window_ids)

time.sleep(5)

# Switch to the new (child) window
for window_id in list_window_ids:
    if window_id != parent_window_id:
        browser.switch_to.window(window_id)
        print("Switched to child window the ID:", window_id)

    time.sleep(2)
#     verify the window title
expected_title = "Human Resources Management Software | OrangeHRM HR Software"
if browser.title == expected_title:
    print("Switched to the correct window.")
else:
    print("This is not expected window")

    time.sleep(2)

#/ locate contact sale web element and click on it

# browser.find_element(By.XPATH,"(//button[@class='btn btn-ohrm btn-free-demo'])[2]").click()
# browser.close()


# switch back to original / parent window
browser.switch_to.window(parent_window_id)







browser.quit()