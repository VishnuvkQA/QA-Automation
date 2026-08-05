from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
wait = WebDriverWait(driver,5)

try:

    wait.until(ec.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
    wait.until(ec.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    wait.until(ec.element_to_be_clickable((By.ID,"login-button"))).click()
    wait.until(ec.url_contains("inventory"))

    # Dont use all different types of select on same code.
    dropdown = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,".product_sort_container")))
    dd = Select(dropdown)
    time.sleep(2)
    dd.select_by_value("lohi")
    # time.sleep(2)
    # dd.select_by_index(3)
    # time.sleep(2)
    # dd.select_by_value("hilo")
    time.sleep(3)

    dropdown = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,".product_sort_container")))
    dd = Select(dropdown)
    info = dd.first_selected_option
    print(info.text)

    dropdown = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,".product_sort_container")))
    dd = Select(dropdown)
    all_options = dd.options
    # for option in all_options:
    #     print(f"All available options are {option.text} and {option.get_attribute('value')}")
    options_text = [option.text for option in all_options]
    expected_options = ["Name (A to Z)",
    "Name (Z to A)",
    "Price (low to high)",
    "Price (high to low)"]

    assert options_text==expected_options, f"The expected options are not matching with the current options... we got {options_text}"
    print("All options are matching")

    prices = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR,".inventory_item_price")))
    price_list = [price.text for price in prices]
    print(price_list)
    


finally:
    driver.quit()