from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
try:
# accepting the alert
    alert_btn = wait.until(ec.element_to_be_clickable((By.ID, "alertButton"))).click()
    alert = wait.until(ec.alert_is_present())
    print(alert.text)
    time.sleep(2)
    alert.accept()
    print("Alert is accepted")

# dismissing the alert
    alert_opt = wait.until(ec.element_to_be_clickable((By.ID, "confirmButton"))).click()
    alert = wait.until(ec.alert_is_present())
    print(alert.text)
    time.sleep(2)
    alert.dismiss()
    print("Alert is dismissed")

# Sending reply to the alert prompt
    alert_prompt = wait.until(ec.element_to_be_clickable((By.ID, "promtButton"))).click()
    alert = wait.until(ec.alert_is_present())
    print(alert.text)
    time.sleep(2)
    alert.send_keys("Hyper VK")
    time.sleep(2)
    alert.accept()
    print("Entered name and accepted")

finally:
    driver.quit()