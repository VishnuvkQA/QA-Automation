import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com")
print(driver.title)
time.sleep(5)

#finding an element with its ID
Username_field = driver.find_element(By.CSS_SELECTOR,"#user-name")
Username_field.send_keys("standard_user")

#Finding an element with attributes and tag
Password = driver.find_element(By.CSS_SELECTOR,"input[type='password']")
Password.send_keys("secret_sauce")

#Finding button with class
Login_btn = driver.find_element(By.CSS_SELECTOR, ".submit-button")
Login_btn.click()


time.sleep(2)

# getting all product names  using find elements
products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
print(f"Found {len(products)} Products in Product Page")
for product in products:
    print(product.text)

driver.quit()
