from selenium import webdriver
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.products_page import Productspage
from pages.login_page import LoginPage

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.saucedemo.com/")

Login = LoginPage(driver)
Products = Login.login("standard_user","secret_sauce")
time.sleep(3)

# Products = Productspage(driver)
Products.addbtn()
print(Products.cartbtn())
assert Products.cartbtn() == "1", f"Value should be 1 but it is {Products.cartbtn()}"
print("Test completed Successfully")
driver.quit()

