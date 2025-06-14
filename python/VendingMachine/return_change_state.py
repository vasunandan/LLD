from vending_machine_state import VendingMachineState
from product import Product
class ReturnChangeState(VendingMachineState):
    def __init__(self,vending_machine):
        self.vending_machine = vending_machine
    def select_product(self,product:Product):
        print("Not applicable")
    def insert_money(self,money):
        print("Not applicable")
    def return_change(self):
        change = self.vending_machine.money - self.vending_machine.money
        self.set_state(self.vending_machine.dispense)
        return change
    def dispense_product(self):
        print("Not applicable")