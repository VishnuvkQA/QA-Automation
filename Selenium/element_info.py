# Getting values by using .text

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# options = Options()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com/")
# wait = WebDriverWait(driver,5)
# try:    
#     wait.until(ec.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
#     wait.until(ec.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
#     wait.until(ec.element_to_be_clickable((By.ID,"login-button"))).click()
#     wait.until(ec.url_contains("inventory"))

#     page_title=driver.find_element(By.CSS_SELECTOR,".title")
#     print(page_title.text)

#     products = driver.find_elements(By.CSS_SELECTOR,".inventory_item_name ")
#     for product in products:
#         print(product.text)
# finally:
#     driver.quit()

# Getting values by using get_attributes()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# options = Options()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com/")
# wait = WebDriverWait(driver,5)
# try:    
#     login_btn = driver.find_element(By.ID,"login-button")
#     print(login_btn.get_attribute("class"))

    
# finally:
#     driver.quit()

# QA use case example (checking the sent value)
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# options = Options()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com/")
# wait = WebDriverWait(driver,5)
# try:    
#     username = driver.find_element(By.ID,"user-name")
#     username.send_keys("standard_user")
#     expected_value = username.get_attribute("value")
#     assert expected_value == "standard_user",  f"Expected values is 'standard_user' but we got {expected_value}"

    
# finally:
#     driver.quit()

# checking if page is visible
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# options = Options()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com/")
# wait = WebDriverWait(driver,5)
# try:    
#     wait.until(ec.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
#     wait.until(ec.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
#     wait.until(ec.element_to_be_clickable((By.ID,"login-button"))).click()
#     wait.until(ec.url_contains("inventory"))

#     page_title=driver.find_element(By.CSS_SELECTOR,".title")
#     print(page_title.is_displayed())
# finally:
#     driver.quit()

#Checking error msg using displayed (real use case)

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# options = Options()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com/")
# wait = WebDriverWait(driver,5)
# try:    
#     driver.find_element(By.ID,"user-name").send_keys("wronguser")
#     driver.find_element(By.ID,"password").send_keys("wronguser")
#     driver.find_element(By.ID,"login-button").click()

#     error = driver.find_element(By.CSS_SELECTOR,"[data-test='error']")
#     assert error.is_displayed(), "Error message to be displayed"
#     print(f"Error : {error.text}")

    
# finally:
#     driver.quit()

# Enabled() in selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# options = Options()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com/")
# wait = WebDriverWait(driver,5)
# try:    
#     login_btn = driver.find_element(By.ID,"login-button")
#     print(login_btn.is_enabled())

    
# finally:
#     driver.quit()

# Small task after combining all

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

option = Options()
option.add_argument("--start-maximized")
driver = webdriver.Chrome(options=option)
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver,5)

# login
try: 
    wait.until(ec.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(ec.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(ec.element_to_be_clickable((By.ID,"login-button"))).click()
    wait.until(ec.url_contains("inventory"))

# Verify we are in products page after login
    title = driver.find_element(By.CSS_SELECTOR, ".title")
    

# Checking title text
    assert title.text=='Products', f"Expected title is products but we got '{title.text}'"
    print(f"Product page title is correct - {title.text}")

# Checking title is displayed
    assert title.is_displayed(), f"Title name should be displayed properly"
    print("Title is displayed")

# Check product count
    products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
    assert len(products)==6, f"Expected product count is 6 but we got'{len(products)}'"
    print(f"Found correct number of products - {len(products)}")

# checking the name of the first product
    f_name = products[0].text
    assert f_name == "Sauce Labs Backpack", f"Expected product name is Sauce Labs Backpack but we got {f_name}  "
    print(f"Got the correct product name {f_name}")

# checking cart button is enabled or not using is_enabled()
    cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    assert cart.is_enabled(), "Add cart to button should be usable"
    print("Add to cart button is enabled")
finally:
    driver.quit()