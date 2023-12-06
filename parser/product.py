class Product():
    title: str = ''
    price: str = '0'
    link: str = ''
    description: str = ''

    def __init__(self, title: str, link: str, price: str = '0', description: str = '') -> None:
        self.price = price
        self.title = title
        self.description = description
        self.link = link

    def format(self) -> str:
            return f'''
                Название: {self.title}\n
                Цена: {self.price}\n
                Ссылка: {self.link}\n
                Описание: {self.description}\n'''
    
    def to_dict(self) -> dict:
        return {
            "price": self.price,
            "title": self.title,
            "description": self.description,
            "link": self.link
        }
    
    def to_list(self) -> list:
        return list(self.to_dict().values())
    
    def set_price(self, price) -> 'Product':
         self.price = price
         return self
    
    def set_description(self, description) -> 'Product':
         self.description = description
         return self