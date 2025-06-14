from vending_machine_state import VendingMachineState
from product import Product
class DispenseState(VendingMachineState):
    def __init__(self,vending_machine):
        self.vending_machine = vending_machine
    def select_product(self,product:Product):
        print("Not applicable")

    def insert_money(self,money):
        print("Not applicable")
    def return_change(self):
        print("Not applicable")
    def dispense_product(self):
        print(f"Product {self.vending_machine.curr_product} dispensed")
        self.vending_machine.set_state(self.vending_machine.idle)