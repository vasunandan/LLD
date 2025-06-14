from abc import ABC
from vehicle_type import VehicleType

class Vehicle(ABC):
    def __init__(self,vehicle_type:VehicleType,plate_no:str):
        self.plate_no = plate_no
        self.vehicle_type = vehicle_type
        self.owner = ""
    def get_plate_no(self):
        return self.plate_no
    def get_vehicle_type(self):
        return self.vehicle_type

