import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

from Part1_Basics.LocatorPractice import forget_pwd

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
#open url
def forgotten_password():
    driver.get("https://www.facebook.com/")
    time.sleep(2)
    try:
        forgotten_click = driver.find_element(By.ID, "u_0_6_d2")
        forgotten_click.click()
        time.sleep(2)
    except Exception as e:
        print("Error:", e)

# successful_login()
forgotten_password()
time.sleep(5)
driver.quit()