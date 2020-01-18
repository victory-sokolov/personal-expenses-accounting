from Parser1188 import Parser1188


class SearchCategory(Parser1188):

    def __init__(self, category):
        self.url = f'https://www.1188.lv/en/catalog/search?InfopageSearch%5Bwhat%5D={category}'
        self.category = category

    def get_branch_by_shop_name(self):
        categories = []
        page = super().get_page()
        branches = page.find_all("div", {"class": "branch"})
        for cat in branches:
            categories.append(cat.find('a').text)
        return categories


search_category = SearchCategory("RIMI")
print(search_category.get_branch_by_shop_name())
