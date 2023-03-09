#!/usr/bin/env python3
from time import sleep
from driver import WebDriver
from web_scraper import WebScraper

web_driver = WebDriver()
scraper = WebScraper()

links = scraper.links
prices = scraper.prices
addresse = scraper.addresses

for idx in range(len(links)):
    if idx == 0: continue
    data = (addresse[idx], prices[idx], links[idx])
    web_driver.chrome_driver(data)
