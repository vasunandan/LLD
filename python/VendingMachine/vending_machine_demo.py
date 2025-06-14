from vending_machine import VendingMachine
from product import Product
from inventory import Inventory

chips = Product("chips",10)
inventory = Inventory()
inventory.add_product(chips,5)

vending_machine = VendingMachine(inventory)
vending_machine.select_product(chips)


