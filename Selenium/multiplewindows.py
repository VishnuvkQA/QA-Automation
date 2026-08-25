from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains as ac
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)
driver.maximize_window()

driver.get("https://demoqa.com/browser-windows")

try:
    #saving the original window
    og_window = driver.current_window_handle
    print(f"Original window {og_window}")

    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@id='tabButton']"))).click()

    wait.until(ec.number_of_windows_to_be(2))
    print(len(driver.window_handles))

    all_windows = driver.window_handles
    time.sleep(2)
    for window in all_windows:
        if window != og_window:
            driver.switch_to.window(window)
            break
    time.sleep(2)
    heading = wait.until(ec.visibility_of_element_located((By.ID, "sampleHeading")))
    assert driver.current_url == "https://demoqa.com/sample"
    print(f"Current url is correct:{driver.current_url}")
    time.sleep(2)
    driver.close()

    driver.switch_to.window(og_window)

    time.sleep(2)

finally:
    driver.quit()