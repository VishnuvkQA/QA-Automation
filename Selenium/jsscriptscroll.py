from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains  as ac
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)
driver.maximize_window()
# driver.get("https://www.saucedemo.com/")
driver.get("https://demoqa.com/frames") #for i frames


try:
    #using pixel scrolling down with js
    # wait.until(ec.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    # wait.until(ec.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    # wait.until(ec.element_to_be_clickable((By.ID, "login-button"))).click()
    # driver.execute_script("window.scrollBy(0,100);")
    # time.sleep(5)
    # print("Scrolled down to 500 pixels")

    #scrolling to bottom and coming back to top
    # wait.until(ec.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    # wait.until(ec.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    # wait.until(ec.element_to_be_clickable((By.ID, "login-button"))).click()
    # driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    # time.sleep(3)
    # print("Scrolled to the bottom of the page")
    # driver.execute_script("window.scrollTo(0,0);")
    # time.sleep(3)
    # print("Scolled up to top again")

    #scrolling to a specific element and bringing it into view
    # main_tab = driver.current_window_handle
    # wait.until(ec.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    # wait.until(ec.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    # wait.until(ec.element_to_be_clickable((By.ID, "login-button"))).click()
    # element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a[href='https://www.linkedin.com/company/sauce-labs/']")))
    # driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # old_window = driver.window_handles
    # actions = ac(driver)
    # actions.move_to_element(element).click().perform()
    # time.sleep(2)
    # wait.until(ec.number_of_windows_to_be(2))
    # for handle in driver.window_handles:
    #     if handle != main_tab:
    #         tab2 = handle
    #         break
    # driver.switch_to.window(tab2)
    # time.sleep(2)
    # print(driver.current_url)
    # driver.close()
    # driver.switch_to.window(main_tab)
    # print("Successfully returned to main tab")
    # time.sleep(2)

    #javascript examples and uses
    # wait.until(ec.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    # wait.until(ec.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    # wait.until(ec.element_to_be_clickable((By.ID, "login-button"))).click()
    # title = driver.execute_script("return document.title;")
    # print(title)
    # scroll = driver.execute_script("return window.pageYOffset;")
    # print(scroll)
    # title = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='item_0_title_link']/div")))
    # driver.execute_script("arguments[0].style.border='3px solid red'",title)
    # time.sleep(5)
    # driver.execute_script("arguments[0].style.border=''",title)
    # time.sleep(2)

    #switching iframes
    # word = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='sampleHeading']")))
    # print(word.text)   #error bcoz not in iframe
    iframe = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='frame2']")))
    driver.switch_to.frame(iframe)
    word = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='sampleHeading']")))
    driver.execute_script("arguments[0].style.border='3px solid black'",word)
    time.sleep(3)
    driver.execute_script("arguments[0].style.border=''",word)
    time.sleep(3)
    print(word.text)
finally:
    driver.quit()

