import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from pages.login_page import LoginPage

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://www.saucedemo.com/")

loginpage = LoginPage(driver)
loginpage.login("standard_user","secret_sauce")

assert "inventory" in driver.current_url, f"Expected is inventory but got {driver.current_url}"
print("Success")
driver.quit()
