import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
browser = webdriver.Chrome()
browser.maximize_window()

wait = WebDriverWait(browser, 10)

# Open URL
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait for title
wait.until(EC.title_contains("OrangeHRM"))

print("Current title:", browser.title)

# Parent window
parent_window_id = browser.current_window_handle
print("Parent window id:", parent_window_id)

# Click OrangeHRM, Inc link
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "OrangeHRM, Inc"))).click()

# Wait for new window
wait.until(EC.number_of_windows_to_be(2))

# Get all window IDs
all_windows = browser.window_handles
print("All windows:", all_windows)

# Switch to child window
for win_id in all_windows:
    if win_id != parent_window_id:
        browser.switch_to.window(win_id)
        print("Switched to child window:", win_id)
        break

# Verify expected title
expected_title = "Human Resources Management Software | OrangeHRM"
wait.until(EC.title_contains("OrangeHRM"))

if browser.title == expected_title:
    print("Correct window!")
else:
    print("Not expected window.")

# Click "Contact Sales"
# wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[text()='Contact Sales'])[1]"))).click()

# Switch back to parent
browser.switch_to.window(parent_window_id)
print("Switched back to parent.")


username = browser.find_element(By.NAME, "username")
username.send_keys("Admin")

password = browser.find_element(By.NAME, "password")
password.send_keys("admin123")

login = browser.find_element(By.TAG_NAME, "button")
login.click()


time.sleep(10)

browser.quit()
