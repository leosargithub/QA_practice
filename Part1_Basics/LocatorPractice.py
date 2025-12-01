#import webdriver module
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from Part1_Basics.Basic_locater import username

#Instantiate webdriver and lunch chrome browser
driver = webdriver.Chrome()


#maximize
driver.maximize_window()
time.sleep(1)


def successful_login():
    # open url
    driver.get("https://practice.expandtesting.com/login")
    userName = "practice"
    Password = "SuperSecretPassword!"
    # enter username
    # find element method is use to locate first matching method
    # username = driver.find_element(By.ID,value="username")
    # username = driver.find_element(By.TAG_NAME,value="input")
    username = driver.find_element(By.CLASS_NAME, value="form-control")
    username.send_keys(userName)
    time.sleep(2)

    # locate Passwrod
    password = driver.find_element(By.NAME, value="password")
    password.send_keys(Password)
    time.sleep(2)

    # locate login button
    # loginBtn = driver.find_element(By.XPATH, value="//button[@type='submit']")

    # using partial class name using Contains mehtod
    # loginBtn = driver.find_element(By.XPATH, value="//button[contains(@class,'btn-primary')]")
    # loginBtn = driver.find_element(By.XPATH, value="//button[text()='Login']")
    loginBtn = driver.find_element(By.XPATH, value="//button[@type='submit' and contains(@class, 'btn-primary')]")
    loginBtn.click()
    time.sleep(3)


# def forget_pwd():
#     # Open Facebook login page
#     driver.get("https://www.facebook.com/")
#     time.sleep(2)  # Wait for page to load completely
#
#     # Locate the "Forgotten password?" link using exact text
#     # driver.find_element(By.ID, value= "email").send_keys("budhathokisaroj827@gmail.com")
#     # time.sleep(7)  # Let the result page load and stay visible
#     driver.find_element(By.LINK_TEXT, "Forgotten password?").click()


# Call the function
#forget_pwd()
def forgotten_password():
    #open url
    driver.get("https://www.facebook.com/")
    time.sleep(5) #wait for 5 sec
    #locate forgotton password link
    # forgottonPwdLink = driver.find_element(By.LINK_TEXT,"Forgotten password?")
    # forgottonPwdLink.click()
   # driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
    #driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()
    #driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
    wait = WebDriverWait(driver, 10)
    forgot_link = driver.find_element(By.XPATH, "//a[contains(text(),'Forgot')]")
    forgot_link.click()

    time.sleep(5)  #wait for 5 sec
    # driver.find_element(By.XPATH, "(//input)[1]").send_keys("example@gmail.com")
    # driver.find_element(By.XPATH, "(//input)[2]").send_keys("demo123@")
    # time.sleep(4)
    driver.find_element(By.XPATH, "//input[@id='identify_email' and @name='email']").send_keys("example@gmail.com")
    time.sleep(3)
#forgotten_password()
def css_selector():
    # open url
    driver.get("https://practice.expandtesting.com/login")
    userName = "practice"
    Password = "SuperSecretPassword!"
    #driver.find_element(By.CSS_SELECTOR, "input").send_keys(userName)
    # driver.find_element(By.CSS_SELECTOR, "[name='username']").send_keys(userName)
    driver.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(userName)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(Password)
    time.sleep(2)
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary" )
    time.sleep(2)

    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(3)


#css_selector()
def css_selector2():
    driver.get("https://www.facebook.com/")

    wait = WebDriverWait(driver, 10)
    forgot_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div > a._97w4")))
    forgot_link.click()

    time.sleep(5)

css_selector2()
#close browser
driver.quit()