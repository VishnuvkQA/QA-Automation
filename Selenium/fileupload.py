import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
option = Options()
option.add_experimental_option("prefs", {"download.default_directory" : r"C:\Users\Vishnu kumar\Music", "download.prompt_for_download" : False})
driver = webdriver.Chrome(options=option)
wait = WebDriverWait(driver,5)
driver.maximize_window()
driver.get("https://demoqa.com/upload-download")

#saving the path of the file we are going to upload
# file = "C:/Users/Vishnu kumar/Downloads"   #we can also use "r" which is spcl string before the orginal path so that we dont need to chang \ to /
# upload_btn = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='uploadFile']")))
# upload_btn.send_keys(file)
# time.sleep(3)
# print("File uploaded successfully")

#creating a test file to upload on automation 
# with open("test_data.txt", "w") as f:
#     f.write("This is the test file to upload for automation\n")
#     f.write("Test file created succesfully\n")

# file = os.path.abspath("test_data.txt")
# upload_btn = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='uploadFile']")))
# upload_btn.send_keys(file)
# time.sleep(3)
# print("File uploaded successfully")

#Downloading a file - we can use request library from python 
# import requests
# dbtn = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='downloadButton']")))
# download_url = dbtn.get_attribute("href")
# response = requests.get(download_url)
# with open("downloaded.pdf", "wb") as f:
#     f.write(response.content)

#downloading by just clicking and downloading it to our own specified path

dbtn = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='downloadButton']"))).click()
print("download succesfull")
time.sleep(4)
driver.quit()