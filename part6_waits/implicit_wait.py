
from selenium import  webdriver
from selenium.webdriver import Keys

from  selenium.webdriver.common.by import By

import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from  selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window()

# add wait for 10 sec
browser.implicitly_wait(10)

browser.get("https://duckduckgo.com/")


# search_input = browser.find_element(By.ID, "searchbox_input")
# search_input = browser.find_element(By.NAME, "q")


# Use explict wait to locate the search box
wait = WebDriverWait(browser, 10)
search_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_input.send_keys("selenium")



# press enter key to submit the search string
search_input.send_keys(Keys.RETURN)


time.sleep(5)
browser.quit()