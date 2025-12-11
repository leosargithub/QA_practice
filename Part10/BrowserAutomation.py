from selenium import  webdriver
from selenium.webdriver.common.by import By
import time


# launch browser & maximize window
browser = webdriver.Chrome()


# open url
browser.get("https://the-internet.herokuapp.com/windows")

# get the unique ID of the current active browser window
parent_window_id = browser.current_window_handle
print("Parent window id: ", parent_window_id)

# locate click here link web element and then perform click action
browser.find_element(By.LINK_TEXT, "Click Here").click()

# Get all window handles (IDs) after new window is opened
list_window_ids = browser.window_handles
print("All windows ids: ", list_window_ids)


# switch to the new (child) window
for window_id in list_window_ids:
    if window_id != parent_window_id:
        browser.switch_to.window(window_id)
        print("Switched to child window with ID:", window_id)


# verify the new window by checking the new
expected_title = "New Window"
if browser.title == expected_title:
    print("Switched to the correct window")
else:
    print("This is not the expected window.")


#     Verify the window by checking the URL
expected_url = "https://the-internet.herokuapp.com/windows/new"
if browser.current_url == expected_url:
    print("Switched to the correct winodw.")
else:
    print("This is not the expected window.")




time.sleep(4)
browser.quit()

