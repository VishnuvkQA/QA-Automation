import os
import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException #u can import exceptions separately or also as a whole
from selenium.common import exceptions

try:
    driver = webdriver.Chrome()
    Wait = WebDriverWait(driver,5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    # driver.get("https://demoqa.com/text-box") 
    
    

#     #Ex of No such element exceptions
#     box = driver.find_element(By.ID, "something")

# except NoSuchElementException as e:
#     print("No such element exception occurred")
#     print(f"Details = {e.msg}")

    #Ex of Timeout exception
#     box = Wait.until(ec.visibility_of_element_located((By.ID, "something")))

# except exceptions.TimeoutException as e:
#     print("Timeout exception occurred")
#     print(f"Details = {e}")  #timout doest have and msg to show so we cant use e.msg

    #Ex of staleelement exceptions
    # box = driver.find_element(By.ID, "userName")
    # driver.refresh()
    # time.sleep(3)
    # try:
    #     box.send_keys("hello")
    # except exceptions.StaleElementReferenceException as e:
    #     print("Staleelementreference exceptions occured: pls refind or relocate the element")
    #     print(f"Details = {e}")

    #     box = driver.find_element(By.ID, "userName")
    #     box.send_keys("Hello")
    #     time.sleep(3)
    #     print("Element relocated and values sent again successfully")

    btn = Wait.until(ec.visibility_of_element_located((By.ID, "login-button")))
    try:
        btn.click()
        time.sleep(3)
    except exceptions.ElementNotInteractableException :
        print("Element is not interactable use js script to click or bring it into view")

        driver.execute_script("arguments[0].click();",btn)
        time.sleep(3)
finally:
    driver.quit()