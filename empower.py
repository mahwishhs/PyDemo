from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#enter your empower credetionals so that login could be successful
trackingNumber = "576854"
password = "FCempowerMS.99"

print("Initializing...")
# using Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://empower.fccollege.edu.pk/fusebox.cfm")

#Entering credentials in the input box using their xpath
driver.find_element(By.XPATH, '//*[@id="empower_usrn"]').send_keys(trackingNumber )
driver.find_element(By.XPATH, '//*[@id="empower_pswd"]').send_keys(password)

#Path for the login button
driver.find_element(By.XPATH, '//*[@id="login-form-no-msg"]/form/div[6]/input[3]').click()
Page_title = driver.title
sleep(4)
#print(Page_title)

if Page_title =='Program Menu - FRM_PROD DB v.3.88.0 Web v.3.88.0':
    print("Login SUCCESSFUL!")
else:
    print("Login FAILED")
