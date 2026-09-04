import os
import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains as ac

driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)
driver.maximize_window()
driver.get("https://www.saucedemo.com")

#creating a reusable function to locate dynamic data
def add_to_cart(driver,wait,data):
    btn = f"add-to-cart-{data}"
    btn_loc = wait.until(ec.element_to_be_clickable((By.ID, btn)))
    btn_loc.click()
def get_by_name(driver,wait,product_name):
    return wait.until(ec.visibility_of_element_located((By.XPATH, f"//div[text()='{product_name}']")))

try:
    wait.until(ec.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(ec.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(ec.element_to_be_clickable((By.ID, "login-button"))).click()
    wait.until(ec.url_contains("inventory"))
    time.sleep(2)

    #Using test data (stable part)
    dropdown = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='product-sort-container']")))
    print(f"Product dropdown is found : {dropdown}")

    #using text content
    product = get_by_name(driver,wait,"Sauce Labs Backpack")
    print(f"Product name is  : {product.text}")
    time.sleep(2)
    #using the parameterized locator (we created the function above)
    add_to_cart(driver,wait,"sauce-labs-backpack")
    print("Name is correct")
    add_to_cart(driver,wait,"sauce-labs-bike-light")

finally:
    driver.quit()