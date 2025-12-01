from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(1)

#find all input fields (Username & Password) using find_elements ()
input_fields = driver.find_elements(By.TAG_NAME, value="input")

#find index of username and password
# print(input_fields[0].get_attribute('id'))
# print(input_fields[1].get_attribute('id'))
# print(input_fields[2].get_attribute('id'))
index = 0
for field in input_fields :
    print(f"Indes: {index}: {field.get_attribute('id')}")
    index = index + 1

input_fields[0].send_keys("standard_user")
time.sleep(2)
# password = driver.find_element(By.ID, value="password")
#password = driver.find_element(By.XPATH, value="//input[@id ='password']")
input_fields[1].send_keys("secret_sauce")
time.sleep(2)

input_fields[2].click()

#list all the products
products = driver.find_elements(By.XPATH, value="//div[@class ='inventory_item_name ']")

print("ProductList")
for product in products:
    print(product.text)

time.sleep(4)

driver.quit()

