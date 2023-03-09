#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# CONFIG
WEB_URL = "https://practicetestautomation.com/practice-test-login/"
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("no-sandbox")
options.add_argument("window-size=1020x800")
options.add_argument("disable-gpu")

# INITIAZE DRIVER FOR HEADLESS CHROME
driver = webdriver.Chrome(options=options)
driver.get(WEB_URL)
#print(driver.title)

# FIND ELEMENT
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
button = driver.find_element(By.CLASS_NAME, "btn")
# SIGN UP USING SENDKEYS AND CLICK CMD
username.send_keys("student")
username.send_keys(Keys.ENTER)

password.send_keys("Password123")
password.send_keys(Keys.ENTER)

button.click()

# CLOSE THE CHROME HEADELESS
driver.quit()
