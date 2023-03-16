#!/usr/bin/env python3
import requests

ENDPOINT = "https://api.npoint.io/1bfdbd4fe4fc82cf75f4"

class Post:
    """ Fetchs Post Data from endpoint """
    def __init__(self):
        self.api_endpoint = ENDPOINT
        
    def fetch_all(self):
        res = requests.get(url=self.api_endpoint)
        return res.json()

    def fetch_by_id(self,_id):
        data = self.fetch_all()
        return data[_id]

