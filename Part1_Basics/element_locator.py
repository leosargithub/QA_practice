from selenium import  webdriver
import time
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.saucedemo.com")

time.sleep(2)

#locate username web element
# username = browser.find_element(By.NAME, "user-name")
# username = browser.find_element(By.XPATH, "(//input[@id='user-name'])[1]")
username = browser.find_element(By.CSS_SELECTOR, "#user-name")


#enter username
username.send_keys("standard_user")

time.sleep(2)

password = browser.find_element(By.NAME, "password")


#enter password
password.send_keys("secret_sauce")


#button click
loginBtn = browser.find_element(By.NAME, "login-button")


loginBtn.click()
time.sleep(2)


# add to cart
# add_to_cart = browser.find_element(By.XPATH, "//button[contains(@id,'sauce-labs-backpack')]")
# add_to_cart = browser.find_element(By.XPATH, "//div[text() ='Sauce Labs Bolt T-Shirt']")
add_to_cart = browser.find_element(By.XPATH,"//div[contains(text() ,'Light')]")
add_to_cart.click()
time.sleep(2)
add_item = browser.find_element(By.XPATH,"//button[text() ='Add to cart']")
add_item.click()
time.sleep(5)
#close browser
browser.quit()
