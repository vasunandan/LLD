from vehicle import Vehicle
from vehicle_type import VehicleType
class Cycle(Vehicle):
    def __init__(self,license_plate:str):
        super().__init__(VehicleType.CYCLE,license_plate)