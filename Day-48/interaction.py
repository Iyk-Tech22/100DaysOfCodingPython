#!/usr/bin/python3
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

# CONFIG
WEB_URL = "https://en.wikipedia.org/wiki/Main_Page"
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("no-sandbox")
options.add_argument("disable-gpu")
options.add_argument("window-size=1020x800")

# CONNECTING DRIVER TO HEADLESS CHROME
driver = webdriver.Chrome(options=options)

# INITIALIZE DRIVER FOR CMDS
driver.get(WEB_URL)

# FIND ELEMENTS
static_tag = driver.find_element(By.XPATH, "//div[@id='articlecount']/a[1]")
print(static_tag.text)
#SEND CLICK CMDS
#static_tag.click()
MediaWiki = driver.find_element(By.LINK_TEXT, "MediaWiki")
MediaWiki.click()

# CLOSE HEADLESS CHROME
#driver.quit()
