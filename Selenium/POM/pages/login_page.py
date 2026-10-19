from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.products_page import Productspage
class LoginPage:

    #Locators we are going to use in login page:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_btn = (By.XPATH, "//*[@id='login-button']")
    error_msg = (By.CSS_SELECTOR, "[data-test='error']")

    #Creating functions to make an action:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        self.wait.until(ec.visibility_of_element_located(self.username_input)).send_keys(username)
        return self
    def enter_pass(self, password):
        self.wait.until(ec.visibility_of_element_located(self.password_input)).send_keys(password)
        return self
    def click_btn(self):
        self.wait.until(ec.element_to_be_clickable(self.login_btn)).click()
        return self

    #Calling the function that we created
    def login(self, username, password):
        self.enter_username(username)
        self.enter_pass(password)
        self.click_btn()
        return Productspage(self.driver)

    def errormsg(self):
        emsg = self.wait.until(ec.visibility_of_element_located(self.error_msg))
        return emsg.text

    def is_error_displayed(self):
        try:
            emsg = self.driver.find_element(*self.error_msg)
            return emsg.is_displayed()
        except:
            return False

    
        