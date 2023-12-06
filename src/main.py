import os
from dotenv import load_dotenv

from chromedriver import Chromedriver
from parser.service.avito import AvitoParser
from writter.csv import CsvWritter

load_dotenv()

chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')
chrome_binary_path = os.getenv('CHROME_BINARY_PATH')

chromedriver = Chromedriver(chrome_driver_path, chrome_binary_path)

print("Включить headless режим (y|n)?")
headlessMode = str(input()).lower() == 'y'

chromedriver.headless = headlessMode
driver = chromedriver.driver()

urlList = {
       "protsessory": "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/protsessory-ASgBAgICAkTGB~pm7gniZw?cd=1&f=ASgBAgECAkTGB~pm7gniZwFFxpoMFXsiZnJvbSI6MCwidG8iOjEwMDAwfQ",
       "materinskie_platy": "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/materinskie_platy-ASgBAgICAkTGB~pm7gnOZw?cd=1&f=ASgBAgECAkTGB~pm7gnOZwFFxpoMFHsiZnJvbSI6MCwidG8iOjc1MDB9",
       "operativnaya_pamyat": "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/operativnaya_pamyat-ASgBAgICAkTGB~pm7gnYZw?f=ASgBAgECAkTGB~pm7gnYZwFFxpoMFHsiZnJvbSI6MCwidG8iOjQwMDB9",
       "sistemy_ohlazhdeniya": "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/sistemy_ohlazhdeniya-ASgBAgICAkTGB~pm7gn2Zw?cd=1&f=ASgBAgECAkTGB~pm7gn2ZwFFxpoMFHsiZnJvbSI6MCwidG8iOjEzMDB9",
       "zhestkie_diski": "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/zhestkie_diski-ASgBAgICAkTGB~pm7gmwZw?f=ASgBAgECAkTGB~pm7gmwZwFFxpoMFHsiZnJvbSI6MCwidG8iOjEzMDB9",
       "bloki_pitaniya": "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/bloki_pitaniya-ASgBAgICAkTGB~pm7gmcZw?cd=1&f=ASgBAgECAkTGB~pm7gmcZwFFxpoMFHsiZnJvbSI6MCwidG8iOjIwMDB9",
       "videokarty": "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1&f=ASgBAgECAkTGB~pm7gmmZwFFxpoMFXsiZnJvbSI6MCwidG8iOjQwMDAwfQ",
       "korpusy": "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/korpusy-ASgBAgICAkTGB~pm7gnEZw?cd=1&f=ASgBAgECAkTGB~pm7gnEZwFFxpoMFHsiZnJvbSI6MCwidG8iOjMwMDB9",
}

avitoParser = AvitoParser(driver=driver)
avitoParser.urlList = [urlList['korpusy']]
writter = CsvWritter('./storage/products.csv')
avitoParser.parse().write(writter)

if headlessMode == True:
    driver.close()