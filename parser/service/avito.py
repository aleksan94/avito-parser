from typing import List
from parser.service.base import BaseParser
from parser.product import Product
from selenium.webdriver.common.by import By

class AvitoParser(BaseParser):
    urlList: list = []

    def _parse_handler_(self) -> List[Product]:
        productList = []

        for url in self.urlList:
            self.driver.get(url)
            itemElementList = self.driver.find_elements(By.CSS_SELECTOR, '[data-marker="item"]')
            for itemElement in itemElementList:
                titleElement = itemElement.find_element(By.CSS_SELECTOR, 'h3[itemprop="name"]')
                priceElement = itemElement.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]')
                descriptionElement = itemElement.find_element(By.CSS_SELECTOR, '[class^="iva-item-descriptionStep-"] > p')
                linkElement = itemElement.find_element(By.CSS_SELECTOR, 'a[itemprop="url"]')

                title = titleElement.text.lower()
                price = priceElement.get_attribute('content')
                description = descriptionElement.text.lower().replace(' ', '')
                link = linkElement.text

                product = Product(title=title, price=price, description=description, link=link)
                productList.append(product)

        return productList