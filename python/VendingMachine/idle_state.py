from vending_machine_state import VendingMachineState
from product import Product
class IdleState(VendingMachineState):
    def __init__(self,vending_machine):
        self.vending_machine = vending_machine
    def select_product(self,product:Product):
        if self.vending_machine.inventory.is_available(product):
            self.vending_machine.curr_product = product
            self.vending_machine.set_state(self.vending_machine.insert)
        else:
            print("Product is not available select another one")
    
    def insert_money(self,money):
        print("Not applicable")
    def return_change(self):
        print("Not applicable")
    def dispense_product(self):
        print("Not applicable")