from parking_spot import ParkingSpot
from vehicle import Vehicle
class ParkingLevel:
    def __init__(self,level:int,numSpot:int):
        self.level = level
        self.spots = [ParkingSpot(i) for i in range(numSpot)]
    def park(self,vehicle:Vehicle):
        for spot in self.spots:
            if spot.park(vehicle):
                return True
        return False
    def unpark(self,vehicle:Vehicle):
        for spot in self.spots:
            if spot.get_vehicle() == vehicle:
                spot.unpark()
                return True
        return False
    def availability(self):
        for i,spot in enumerate(self.spots):
            print(i,":",spot.is_avialable())
