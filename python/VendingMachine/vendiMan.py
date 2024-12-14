from product import Product
from typing import List
class VendiMan():
    def __init__(self,max_diff_product:int,max_product:int):
        self.max_diff_product = max_diff_product
        self.max_product = max_product
        self.Machine:List[List[Product]] = [[None]*max_product for i in range(max_diff_product)]
    

    def add_product(self,product_id:int,quantity:int):
        if self.product_id not in range(max_diff_product):
            raise Exception("Product id not available")
        product_added = 0
        for i in range(max_product):
            if self.Machine[product_id][i] is None:
                self.Machine[product_id][i] = Product()
                product_added+=1
        if product_added == 0:
            raise Exception("Respective product is full")
        return product_added
    