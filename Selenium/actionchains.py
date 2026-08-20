from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
Wait = WebDriverWait(driver,5)
driver.maximize_window()
# driver.get("https://www.w3schools.com/howto/howto_css_dropdown.asp") --for hover
# driver.get("https://testautomationpractice.blogspot.com/") #for clicks
# driver.get("https://extendsclass.com/text-compare.html")    #for keyboard actions
driver.get("https://jqueryui.com/droppable/")  #For drag and drop
actions = ActionChains(driver)



try: 
    # trying hover action
    # item = Wait.until(ec.presence_of_element_located((By.XPATH, "//button[@class='dropbtn']")))
    # actions.move_to_element(item).perform()
    # time.sleep(2)
    # item2 = Wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[class='dropdown dropdown2'] a:nth-child(2)")))
    # print(item2.text)
    # time.sleep(2)
    # item2.click()

    # right click
    # rbutton = Wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#PopUp')))
    # actions.context_click(rbutton).perform()
    # print(rbutton.text)
    # time.sleep(3)

    # Doubt click
    # double_click = Wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "button[ondblclick='myFunction1()']")))
    # actions.move_to_element(double_click).double_click().perform()
    # time.sleep(3)

    #Keyboard Actions
    # source = Wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="dropZone"]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div[4]/pre/span'))).click()
    # source= actions.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).perform()
    # time.sleep(5)
    # dest = Wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="dropZone2"]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div[5]/pre/span'))).click()
    # dest = actions.key_down(Keys.CONTROL).send_keys("a").send_keys("v").key_up(Keys.CONTROL).perform()
    # time.sleep(5)

    #tried adding some buttons to action
    # source = Wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="dropZone"]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div[4]/pre/span'))).click()
    # source= actions.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).perform()
    # time.sleep(5)
    # dest = Wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="dropZone2"]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div[5]/pre/span')))
    # dest.click()
    # dest = actions.key_down(Keys.CONTROL).send_keys("a").send_keys(Keys.BACK_SPACE).send_keys("v").key_up(Keys.CONTROL).perform()
    # time.sleep(5)

    driver.switch_to.frame(Wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='content']/iframe"))))
    elem1 = Wait.until(ec.visibility_of_element_located((By.ID, "draggable")))
    elem2 = Wait.until(ec.visibility_of_element_located((By.ID, "droppable")))
    actions.drag_and_drop(elem1,elem2).perform()
    time.sleep(5)
    #we can use coordinates (offsets) to drag and drop as well
finally:
    driver.quit()
