from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

option = Options()
option.add_argument("--start-maximized")
driver = webdriver.Chrome(options=option)
driver.get("https://www.saucedemo.com/")

# Using wait by assigning it to a variable for reuse
wait = WebDriverWait(driver,10)

# locating username field using explicit wait to load the page
username=wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

# locating password field using Explicit wait to load the page
password=wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")

# locating the btn using explicity wait to load the page
login=wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()

# Wait untill the product page loads and verify
wait.until(EC.url_contains("inventory"))
print("Product page loaded successfully")
print(driver.current_url)
driver.quit()