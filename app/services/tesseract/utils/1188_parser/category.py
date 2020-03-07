import csv
import json
import re

import requests
from bs4 import BeautifulSoup

from Parser1188 import Parser1188


class Category(Parser1188):

    def __init__(self, url):
        super().__init__(url)
        self.category_list = {}
        self.category_list['companies'] = []

    def get_category_list(self):
        page = super().get_page()
        content_wrapper = page.find(
            "div", {"id": "letter-content"}).find_all("ul", {"class": "letter-list"})

        for cats in content_wrapper:
            cats_set = cats.text.split("\n")
            for cat in cats_set:
                if len(cat) > 0:
                    self.category_list['companies'].append({
                        'category': cat.replace(" ", ""),
                        'shop': ''
                    })

        with open("companies.json", 'w') as f:
            json.dump(self.category_list, f)


category = Category("https://www.1188.lv/en/catalog")
category.get_category_list()
