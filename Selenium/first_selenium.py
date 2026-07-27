# import selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time

# #Creating options for Chrome (browser)
# options = Options()
# options.add_argument("--start-maximized")

# #Creating browser driver
# driver = webdriver.Chrome(options=options)

# # Opening a website
# driver.get("https://www.saucedemo.com")

# #Using time module to pause the website to see
# time.sleep(5)

# #Printing website title
# print(driver.title)

# #Quiting website
# driver.quit()


# Learning on how to find elements on webpage and enter details to it
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")

# Finding username element and entering details automatically
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

# Finding password element and entering details automatically
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

#Locating login button and clicking
login_button = driver.find_element(By.ID,"login-button")
login_button.click()

# time module to pause the page
time.sleep(10)

# Checking the page title and url to ensure we landed on the correct page
print(driver.title)
print(driver.current_url)

# Quiting the page
driver.quit()