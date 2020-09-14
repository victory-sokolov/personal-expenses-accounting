import json
import os

from project.category.Parser1188 import Parser1188


class SearchCategory(Parser1188):

    def __init__(self, category):
        self.url = f'https://www.1188.lv/en/catalog/search?InfopageSearch%5Bwhat%5D={category}'
        self.category = category

    def get_branch_by_shop_name(self):
        categories = []
        page = super().get_page()
        company = page.find_all("div", {"class": "company"})
        branches = [branch.find("div", {"class": "branch"})
                    for branch in company]

        for cat in branches:
            if cat:
                categories.append(cat.find('a').text)

        return categories[0] if categories else ""
