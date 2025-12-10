from selenium import webdriver


import  time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()

browser.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")


p_text = browser.find_element(By.TAG_NAME, "p")
print(p_text.text)

time.sleep(2)
browser.quit()