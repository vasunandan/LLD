from idle_state import IdleState
from insert_money_state import InsertState
from return_change_state import ReturnChangeState
from dispense_state import DispenseState
from vending_machine_state import VendingMachineState
from product import Product
class VendingMachine:
    _instance = None
    def __init__(self,inventory):
        self.inventory = inventory
        self.idle = IdleState(self)
        self.insert = InsertState(self)
        self.change = ReturnChangeState(self)
        self.dispense = DispenseState(self)
        self.curr_state = self.idle
        self.curr_product = None
        self.money = 0
    def __new__(cls,*args):
        if cls._instance is None:
            cls._instance = super(VendingMachine,cls).__new__(cls)
        return cls._instance
    def set_state(self,state):
        self.curr_state = state
    def update_money(self,m):
        if m not in Money.__members__:
            print("Not acceptable")
        else:
            self.money += m 
    def select_product(self,product:Product):
        self.curr_state.select_product(product)
    def insert_money(self,money):
        self.curr_state.insert_money(money)
    def return_change(self):
        self.curr_state.return_change()
    def dispense_product(self):
        self.curr_state.dispense_product()
    