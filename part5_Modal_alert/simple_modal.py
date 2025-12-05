#import required libraries
from selenium import webdriver

from selenium.webdriver.common.by import By # To locate elements on the webpage
import  time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://practice-automation.com/modals/")
#
# simple_modal = browser.find_element(By.ID, "simpleModal")
# simple_modal.click()
# time.sleep(3)
#
# title = browser.find_element(By.ID, "pum_popup_title_1318")
# print("Title", title.text)
#
# time.sleep(2)
#
# content = browser.find_element(By.XPATH, "(//div[@class='pum-content popmake-content'])[1]").text
# print(f"Model content {content}")
# time.sleep(2)
#
# close_btn = browser.find_element(By.CLASS_NAME, "pum-close ")
# close_btn.click()
# print("closed alert")

# find form modal button
form_modal = browser.find_element(By.ID, "formModal")
form_modal.click()
time.sleep(2)

# Enter name
browser.find_element(By.NAME, "g1051-name").send_keys("Saroj Budhathoki")
time.sleep(2)

browser.find_element(By.ID, "g1051-email").send_keys("imroj@gmail.com")
time.sleep(2)

browser.find_element(By.ID, "contact-form-comment-g1051-message").send_keys("This example messages")

browser.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()




time.sleep(3)
browser.quit()




