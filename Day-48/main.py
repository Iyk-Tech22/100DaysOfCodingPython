#!/usr/bin/python3
""" Testing """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Chrome config
WINDOW_SIZE = "1920x1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(f"window-size={WINDOW_SIZE}")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

# Connecting to webdriver
#service = Service(executable_path=WEB_DRIVER_PATH)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
search_tag = driver.find_element(by=By.NAME, value="q")
print(driver.title)
#print(search_tag.get_attribute("placeholder"))

# FIND ELEMENT CLASS NAME
logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
#print(logo.text)

# FIND ELEMENT XPATH
bug_lnk = driver.find_element(By.XPATH, "//*[@id='site-map']/div[2]/div/ul/li[3]/a")
#print(bug_lnk.text)

# CHALLANGE:: SCRAPE ALL UPCOMING EVENT IN TO DICT
upcoming_events = {}
time_tags = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
name_tags = driver.find_elements(By.CSS_SELECTOR, ".event-widget time+a")

for index,time_tag in enumerate(time_tags):
    #print(time_tag.text)
    upcoming_events[index] = {"time":time_tag.text}

for index,name_tag in enumerate(name_tags):
    #print(name_tag.text)
    upcoming_events[index]["name"] = name_tag.text

print(upcoming_events)
driver.close()
