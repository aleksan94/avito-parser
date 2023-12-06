from typing import List
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from fake_useragent import UserAgent


class Chromedriver:
    driver_path: str = ''
    binary_path: str = ''
    user_agent: str = ''
    # установить в True для headless режима
    headless: bool = False
    # по-умолчанию браузер не закрывается, для закрытия вручную вызываем метод close()
    detach: bool = True

    def __init__(self, driver_path: str = '', binary_path: str = '', user_agent: str = '') -> None:
        self.driver_path = driver_path
        self.binary_path = binary_path
        self.user_agent = user_agent

    def driver(self) -> 'Chrome':
        service = self.__get_service__()
        options = self.__get_options__()
        return webdriver.Chrome(service=service, options=options)
    
    def set_driver_path(self, driver_path) -> 'Chromedriver':
        self.driver_path = driver_path
        return self

    def set_binary_path(self, binary_path) -> 'Chromedriver':
        self.binary_path = binary_path
        return self
    
    def set_user_agent(self, user_agent) -> 'Chromedriver':
        self.user_agent = user_agent
        return self
    
    def __get_service__(self) -> 'Chromedriver':
        service = Service(self.driver_path)
        return service

    def __get_options__(self) -> 'Options':
        options = Options()
        options.binary_location = self.binary_path
        
        # убираем видимость автоматизированного ПО
        # сайт проверки:
        # https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html
        options.add_argument("--disable-blink-features=AutomationControlled")

        if self.headless == True:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            options.add_argument("--no-sandbox")

        if self.detach == True:
            options.add_experimental_option("detach", True)

        user_agent = self.user_agent
        if user_agent == '':
            ua = UserAgent()
            user_agent = ua.random
        options.add_argument(f'--user-agent={user_agent}')

        # ssl
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        return options