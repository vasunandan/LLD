from vehicle import Vehicle
class ParkingSpot():
    def __init__(spot_number:int):
        self.spot_number = spot_number
        self.vehicle_park = None
    def park_vehicle(self,vehicle:Vehicle):
        if self.vehicle_park is None:
            self.vehicle_park = vehicle
            return True
        return False
    def unpark_vehicle(self):
        if self.vehicle_park is not None:
            self.vehicle_park = None
            return True
        return False    
    def is_empty(self):
        return self.vehicle_park is None

