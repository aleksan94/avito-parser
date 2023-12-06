from writter.abstract import AbstractWritter
import csv
import os

class CsvWritter(AbstractWritter):
    file_path: str = ''
    data: list = []

    def __init__(self, file_path: str = '', data: list = []) -> None:
        self.file_path = file_path
        self.data = data

    def _write_handler_(self) -> bool:
        dirname = os.path.dirname(self.file_path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(self.file_path, 'w', encoding="utf-8") as file:
            writter = csv.writer(file, delimiter=';')
            writter.writerows(self.data)
        return 
    
    def set_file_path(self, file_path: str) -> 'CsvWritter':
        self.file_path = file_path
        return self
    
    def set_data(self, data: list) -> 'CsvWritter':
        self.data = data
        return self
    
    def add_item(self, item: any) -> 'CsvWritter':
        self.data.append(item)
        return self