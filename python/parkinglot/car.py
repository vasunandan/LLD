from vehicle import Vehicle
from vehilce_type import VehicleType
class Car(Vehicle):
    def __init__(self,licence_plate:str):
        super().__init__(licence_plates,VehicleType.CAR)