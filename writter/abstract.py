from abc import ABC, abstractmethod

class AbstractWritter(ABC):

    __data__: any

    def __init__(self, data: any) -> None:
        self.__data__ = data
    
    @abstractmethod
    def _write_handler_(self, data: any) -> bool:
        """
        Переопределяемый метод для записи
        """
        pass

    def write(self) -> bool:
        return self._write_handler_()
    
    def set_data(self, data: any) -> 'AbstractWritter':
        self.__data__ = data
        return self
    
    def get_data(self) -> any:
        return self.__data__