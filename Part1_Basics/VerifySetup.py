#import webdriver module from selenium package
from selenium import webdriver

#instantiate webdriver and lunch Chrome browser
driver = webdriver.Chrome()


#open google.com
driver.get("https://www.google.com")
