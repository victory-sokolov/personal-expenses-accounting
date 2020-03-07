import csv
import json
import re

import requests
from bs4 import BeautifulSoup


class Parser1188:

    def __init__(self, url):
        self.url = url

    def get_page(self):
        r = requests.get(self.url)
        page = BeautifulSoup(r.text, "html.parser")
        return page
