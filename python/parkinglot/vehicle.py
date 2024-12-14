from abc import ABC
from vehilce_type import VehicleType
class Vehicle(ABC):
    def __init__(self,licence_plate:str,vehilce_type:VehicleType):
        self.licence_plate = licence_plate
        self.vehilce_type = vehilce_type
    def get_plate(self):
        return self.vehilce_type