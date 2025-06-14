class Product:
    def __init__(self,product_name,price):
        self.name = product_name
        self.price = price
    def get_price(self):
        return self.price
    def get_name(self):
        return self.name