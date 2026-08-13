from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)
# driver.get("https://syntaxprojects.com/basic-checkbox-demo.php")
driver.get("https://syntaxprojects.com/basic-radiobutton-demo.php")
driver.maximize_window()

# Single checkbox

# checkbox = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']")))
# print(checkbox.is_selected())
# time.sleep(2)
# if checkbox.is_selected()==False:
#     checkbox.click()
# time.sleep(2)
# if checkbox.is_selected()==True:
#     checkbox.click()
# time.sleep(2)
# print("Checkbox is unticked")

# Multiple checkboxes
# checkboxes = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']")))
# print(len(checkboxes))
# for check in checkboxes:
#     if not check.is_selected():
#      check.click()
# time.sleep(2)
# print("All checkboxes are ticked")

# radio buttons
radio =     wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='radio'][value='Male']")))
radio.click()
time.sleep(2)
print(radio.is_selected())
radio1 = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='radio'][value='Female']")))
radio1.click()
time.sleep(2)
print(radio1.is_selected())


driver.quit()

# single checkbox
# checkbox = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']")))
# if not checkbox.is_selected():
#     checkbox.click()
# time.sleep(2)
# print(f"checkbox status {checkbox.is_selected()}")
# if checkbox.is_selected():
#     checkbox.click()
#     time.sleep(2)
#     assert  checkbox.is_selected()==False, f"Checkbox should be unticked"
# print(f"Checkbox is unticked after selected earlier...its current status is {checkbox.is_selected()}")
# driver.quit()

# multiple checkboxes
# checkboxes = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, '.checkbox')))
# print(f"Total number of checkboxes are {len(checkboxes)}")

# for check in checkboxes:
#     if not check.is_selected():
#         check.click()
# time.sleep(2)
# for check in checkboxes:
#     assert not check.is_selected(), f"Checks are ticked"
# print(f"Checkboxes are ticked and current status is {check.is_selected()}")

