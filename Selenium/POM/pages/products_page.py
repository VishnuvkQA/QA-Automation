from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Productspage:
        addtocart = (By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
        cart_btn = (By.CLASS_NAME, "shopping_cart_badge")

        def __init__(self, driver):
                self.driver = driver
                self.wait = WebDriverWait(driver,5)

        def addbtn(self):
                return self.wait.until(ec.element_to_be_clickable(self.addtocart)).click()

        def cartbtn(self):
                return self.wait.until(ec.visibility_of_element_located(self.cart_btn)).text