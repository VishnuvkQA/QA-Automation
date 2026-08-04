from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# Opening a website
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
try:
# Logging into website
    wait = WebDriverWait(driver,5)
    wait.until(ec.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    wait.until(ec.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    wait.until(ec.element_to_be_clickable((By.ID,"login-button"))).click()
    time.sleep(2)
    # Checking next page and adding a product
    print(driver.title)
    print(driver.current_url)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(2)

    # going to cart page
    driver.get("https://www.saucedemo.com/cart.html")
    wait.until(ec.url_contains("cart"))
    print(f"We are currently at {driver.current_url} page")
    time.sleep(2)
    # Going back to product page
    driver.back()
    wait.until(ec.url_contains("inventory"))
    print(f"We came back to {driver.current_url} page")
    time.sleep(2)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
    print(f"Product - has been removed")
    time.sleep(2)
    # Refreshing the page
    driver.refresh()
    wait.until(ec.url_contains("inventory"))
    print("Page is refreshed successfully")
    time.sleep(2)
    # Verifying all the products are there after refresh
    products = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,'.inventory_item_name')))
    assert len(products) == 6, f"Products in this page should be six but we got {len(products)}"
    print(f"Total {len(products)} Products are there ")

finally:
    driver.quit()