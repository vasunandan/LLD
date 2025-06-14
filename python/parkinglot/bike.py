from vehicle import Vehicle
from vehicle_type import VehicleType

class Bike(Vehicle):
    def __init__(self,license_plate:str):
        super().__init__(VehicleType.BIKE,license_plate)