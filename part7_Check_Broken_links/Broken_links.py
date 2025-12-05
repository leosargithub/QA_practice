#import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import  requests
browser = webdriver.Chrome()

browser.maximize_window()

# browser.get("https://practice.expandtesting.com/")
browser.get("http://www.deadlinkcity.com/")

# Get all <a> tags
links = browser.find_elements(By.TAG_NAME, "a")
print(f"Total links found: {len(links)}")

# counters
valid_links = 0
broken_links = 0

# Loop through all collected <a> link elements
for link in links:
    # Get the url from the "href" attribute of the <a> tag
    url = link.get_attribute("href")

#     Make an HTTP Head request to given URL
#     exception handling
    try:
        response = requests.head(url)

        if response.status_code >= 400:
          print("Broken Link")
          broken_links += 1


        else:
         print("Valid Link")
         valid_links +=1
    except:
        None

print(f"broken links {broken_links}")
print(f"valid links {valid_links}")




time.sleep(3)
browser.quit()