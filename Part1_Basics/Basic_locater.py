from pickletools import bytes_types

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(1)
#Locate user name web element
#username = driver.find_element(By.NAME, value="user-name")
#username = driver.find_element(By.XPATH, value="//input[@name = 'user-name']")
# username = driver.find_element(By.XPATH,value="//input[@type= 'text' and @id = 'user-name']")
# username = driver.find_element(By.XPATH,value="(//input)[1]")
# username = driver.find_element(By.TAG_NAME, value="input")
# username = driver.find_element(By.CSS_SELECTOR, value="input")
username = driver.find_element(By.CSS_SELECTOR, value="#user-name")
# Enter username
username.send_keys("standard_user")
time.sleep(1)
# password = driver.find_element(By.ID, value="password")
password = driver.find_element(By.XPATH, value="//input[@id ='password']")


password.send_keys("secret_sauce")
time.sleep(1)
# button = driver.find_element(By.ID, value="login-button")
#button = driver.find_element(By.XPATH, value="//input[@id = 'login-button']")
# button = driver.find_element(By.XPATH, value= "//input[@id = 'submit-button' or @id = 'login-button']")
# button = driver.find_element(By.CLASS_NAME, value="btn_action")
# button = driver.find_element(By.CSS_SELECTOR, value=".btn_action")
# button = driver.find_element(By.CSS_SELECTOR, value="input[id='login-button']")
# button = driver.find_element(By.CSS_SELECTOR, value="input.btn_action")
button = driver.find_element(By.CSS_SELECTOR, value="form> input[type='submit']")
button.click()
time.sleep(3)
cart = driver.find_element(By.XPATH, value= "//button[contains(@id,'add-to-cart-sauce-labs-backpack')]")

cart.click()
time.sleep(4)
#locate web element using text method
textCart = driver.find_element(By.XPATH, value= "//div[text()='Sauce Labs Fleece Jacket']")
textCart.click()
time.sleep(5)
# back to
back = driver.find_element(By.XPATH, value="//button[@id='back-to-products']")
back.click()
time.sleep(1)
#partial text using contains method
# partialText = driver.find_element(By.XPATH,value="//div[contains(text(),'Bolt T-Shirt')]")
# partialText.click()
#find product link for sauce labs Backpack using link text

# productLink = driver.find_element(By.LINK_TEXT, value= "Sauce Labs Backpack")
# productLink.click()
# partial link text
productLink = driver.find_element(By.PARTIAL_LINK_TEXT, value= "Backpack")
productLink.click()

time.sleep(3)
driver.quit()