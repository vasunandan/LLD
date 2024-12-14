from parkingspot import ParkingSpot
from vehicle import Vehicle
class Level():
    def __init__(self,level:int,no_of_spots:int):
        self.level = level
        self.list:List[ParkingSpot] = [ParkingSpot(i) for i in range(no_of_spots)]
    def park_vehicle(self,vehicle:Vehicle):
        for spt in self.list:
            if spt.park_vehicle(vehicle): 
                return True
        return False
    def is_available(self):
        for spt in self.list:
            if spt.is_empty():
                return True
        return False
    def unpark_vehicle(self,vehicle:Vehicle):
        for spt in self.list:
            if not spt.vehicle_park and spt.vehicle_park= vehicle:
                spt.vehicle_park = None
                return True
        return False
    
    
