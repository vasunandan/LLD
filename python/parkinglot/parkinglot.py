from typing import List
from level import Level
from vehicle import Vehicle

class ParkingLot():
    _instance = None
    def __init__(self):
        if ParkingLot._instance is None:
            raise("This is singleton class")
        else:
            ParkingLot._instance = self
            self.levels:List[Level] = []


    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            return ParkingLot()
        return ParkingLot._instance