from vehicle import Vehicle
class ParkingSpot:
    def __init__(self,spot_no:int):
        self.spot_no = spot_no
        self.vehicle = None
    def is_avialable(self):
        return self.vehicle is None
    def park(self,vehicle:Vehicle)->bool:
        if self.vehicle:
            return False
        self.vehicle = vehicle
        return True
    def unpark(self):
        self.vehicle = None
    def get_vehicle(self):
        if self.vehicle is None:
            return "Spot is empty"
        return self.vehicle
    def get_spot_no(self):
        if self.vehicle:
            return self.spot_no()
        return ""
