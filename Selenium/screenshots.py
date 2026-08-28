from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from datetime import datetime
import os

driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# #capturing only the element as screenshot
# btn = wait.until(ec.element_to_be_clickable((By.ID,"login-button")))
# btn.screenshot(".\\btn.png")
# print("Btn screenshot is saved")

# #capturing the whole page before
# before = driver.save_screenshot(".\\before.png")
# btn.click()
# time.sleep(3)
# #capturing whole page after error
# after = driver.save_screenshot(".\\after.png")
# time.sleep(2)

#capturing manually as binary 
# btn_pic = driver.get_screenshot_as_png()

# with open("base.png", "wb") as file:
#     file.write(btn_pic)
# print("screenshot saved as binary successfully")

def screenshot_on_failure(driver, testname):
    "Captures screenshot with time and date when an assertion failes"
    timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
    filename = f"Failure_{testname}_{timestamp}.png"


    screenshots_folder = "Selenium/screenshots"
    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)

    filepath = os.path.join(screenshots_folder, filename)
    driver.save_screenshot(filepath)
    print(f"Failed and screenshot save {filepath}")
    return filepath
try:
    wait.until(ec.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(ec.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(ec.element_to_be_clickable((By.ID,"login-button"))).click()
    wait.until(ec.url_contains("inventory"))

    title = driver.find_element(By.CSS_SELECTOR, ".title")
    assert title.text == "products", f"Title should be Products but we got {title.text}"

except AssertionError as ee:
    screenshot_on_failure(driver, "logintest")
    print(f"Test failed {ee}")
    raise
except Exception as e:
    screenshot_on_failure(driver, "exceptionerror")
    print(f"exception error {e}")
    raise
print("Program ran successfully without errors")
driver.quit()


