from product import Product
class Inventory:
    def __init__(self):
        self.Products = {}
    def add_product(self,product:Product,q):
        if product not in self.Products:
            self.Products[product] = q
        else:
            print("Product exists")
    def update(self,product:Product,q):
        if q<0:
            return
        if product not in self.Products:
            print("product is not available")
        else:
            self.Products[product] = q
    def is_available(self,product):
        if product in self.Products and self.Products[product]>0:
            return True
        return False
    
