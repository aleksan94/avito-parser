from abc import ABC, abstractmethod
from typing import List
from selenium.webdriver import Chrome
from parser.product import Product
from writter.abstract import AbstractWritter
from functional import seq

class BaseParser(ABC):
    driver: Chrome
    __products__: List[Product]

    def __init__(self, driver: Chrome) -> None:
        self.driver = driver

    @abstractmethod
    def _parse_handler_(self) -> List[Product]:
        """
        Переопределяемый метод для реализации обработчика парсинга
        """
        pass

    def parse(self) -> 'BaseParser':
        self.__products__ = self._parse_handler_()
        return self
    
    def add_product(self, product: Product) -> 'BaseParser':
        self.__products__.add_item(product)
        return self
    
    def get_products(self) -> List[Product]:
        return self.__products__
    
    def write(self, writter: AbstractWritter) -> 'BaseParser':
        data = seq(self.get_products()).map(lambda product: product.to_list()).to_list()
        writter.set_data(data)
        writter.write()
        pass