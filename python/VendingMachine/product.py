class Product():
    def __init__(self,name:string,price:int):
        self.name = name
        self.price = price
    def get_name(self) -> string:
        return self.name
    def get_price(self) -> string:
        return self.price
    def change_price(self,new_price:int) -> None:
        self.price = new_price
        return
