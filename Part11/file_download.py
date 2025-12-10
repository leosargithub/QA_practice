from selenium import webdriver

from selenium.webdriver.common.by import By

import time

from selenium.webdriver.support.wait import WebDriverWait

# browser open
browser = webdriver.Chrome()


# open url

browser.get("https://practice-automation.com/file-download/")

browser.implicitly_wait(10)

wait = WebDriverWait(browser, 10)

browser.find_element(By.XPATH, "//a[text()='Sandbox Download Form - .pdf']").click()

browser.find_element(By.XPATH, "(//a[contains(@class,'wpdm-download-link')])[1]").click()
time.sleep(5)
browser.quit()