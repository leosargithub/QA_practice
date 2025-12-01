from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("http://selenium.dev/")
browser.maximize_window()
time.sleep(5)

title = browser.title
print(title)
assert "Selenium" in title
