from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
option = Options()
option.add_argument("--start-maximized")
driver = webdriver.Chrome(options=option)
driver.get("https://www.saucedemo.com/")

# Finding and sending values to user field using xpath
driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys("standard_user")

# Finding and sending values to password using xpath
driver.find_element(By.XPATH, "//*[@type='password']").send_keys("secret_sauce")

#Finding and clicking the login vutton using Xpath
driver.find_element(By.XPATH, "//*[@id='login-button']").click()

time.sleep(5)

# Getting all products name using Xpath
products = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name ']")
print(f"Found {len(products)} Products in Product page")

for product in products:
    print(f" - {product.text}")

driver.quit()