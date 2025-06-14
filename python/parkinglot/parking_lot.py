
from parking_level import ParkingLevel
from vehicle import Vehicle
# def singleton(cls):     # decorator for singleton 
#     instances = {}
#     def get_instance(*args,**kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args,**kwargs)
#         return instances[cls]
#     return get_instance


class ParkingLot:
    _instance = None
    def __new__(cls,*args,**kwargs):
        if cls._instance:
            return cls._instance
        cls._instance = super(ParkingLot,cls).__new__(cls)
        return cls._instance
    def __init__(self,levels:int,spots:int):
        self.levels = [ParkingLevel(i,spots) for i in range(levels)]
    def park(self,vehicle:Vehicle):
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False
    def unpark(self,vehicle:Vehicle):
        for level in self.levels:
            if level.unpark(vehicle):
                return True
        return False
    def availability(self):
        for level in self.levels:
            level.availability()