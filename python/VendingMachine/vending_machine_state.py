from abc import ABC,abstractmethod
from product import Product
class VendingMachineState(ABC):
    def __init__(self,inventory):
        self.inventory = inventory
    @abstractmethod
    def select_product(self,product:Product):
        pass
    @abstractmethod
    def insert_money(self,money):
        pass
    @abstractmethod
    def return_change(self):
        pass
    @abstractmethod
    def dispense_product(self):
        pass