
import requests
import web_scraper_config
from bs4 import BeautifulSoup

# REQUESTS SOURCE CODE
URL = web_scraper_config.URL
BASE_URL = web_scraper_config.BASE_URL

class WebScraper:
    """ Scrape site data """
    def __init__(self):
        self.addresses = []
        self.prices = []
        self.links = []
        self.scraper()
    def request_source(self):
        """ Requests website html source code """
        res = requests.get(URL)
        return res.text
    def scraper(self):
        """ Scrape the website data """
        html = self.request_source()
        soup = BeautifulSoup(html, "html.parser")
        links = soup.select(".similar-listings-info a")
        prices = soup.select(".similar-listings-price h4")
        address_tags = soup.find_all("p", class_="listings-location")
        for idx in range(len(address_tags)):
            self.addresses.append(address_tags[idx].get_text()[4:-1])
            self.links.append(f"{BASE_URL}{links[idx].get('href')}")
            self.prices.append(prices[idx].get_text()[1:-1])
