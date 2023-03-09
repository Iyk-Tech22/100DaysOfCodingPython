#!/usr/bin/env python3
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WebDriver:
    # CONFIG
    _url = "https://forms.gle/DSnvzHYL9keBF1sJ7"
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("headless")
        self.options.add_argument("no-sandbox")
        self.options.add_argument("window-size=1020x800")
        self.options.add_argument("disable-gpu")
    def chrome_driver(self, data):
        """ Drivers initiase and manage all activities of the chrome headless browser """
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self._url)
        sleep(3)
        self.submit_tag = self.driver.find_element(By.CSS_SELECTOR, "div.lRwqcd div[role]")
        self.input_tags = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        self.address_tag = self.input_tags[0]
        self.price_tag = self.input_tags[1]
        self.link_tag = self.input_tags[2]
        self.send_inputs(data)
        self.submit_form()
        self.driver.quit()
    def send_inputs(self, texts):
        """ Send all keys to the browser """
        self.address_tag.send_keys(texts[0])
        self.address_tag.send_keys(Keys.ENTER)
        self.price_tag.send_keys(texts[1])
        self.price_tag.send_keys(Keys.ENTER)
        self.link_tag.send_keys(texts[2])
        self.link_tag.send_keys(Keys.ENTER)
    def submit_form(self):
        """ Submit the form """
        self.submit_tag.click()

