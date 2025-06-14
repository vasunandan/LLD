from vending_machine_state import VendingMachineState
from product import Product
class InsertState(VendingMachineState):
    def __init__(self,vending_machine):
        self.vending_machine = vending_machine
    def select_product(self,product:Product):
        print("Not applicable")

    def insert_money(self,money):
        self.vending_machine.update_money(money)
        if select.vending_machine.money >= product.get_price():
            self.vending_machine.set_state(self.vending_machine.change)
    def return_change(self):
        print("Not applicable")
    def dispense_product(self):
        print("Not applicable")