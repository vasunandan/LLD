from parking_lot import ParkingLot
from car import Car
from bike import Bike
from cycle import Cycle
parkinglot = ParkingLot(2,1)
vehicle_1 = Car("A1234")
vehicle_2 = Bike("B134")
vehicle_3 = Cycle("C212")
print(parkinglot.park(vehicle_1))
print(parkinglot.park(vehicle_2))
print(parkinglot.park(vehicle_3))
print(parkinglot.unpark(vehicle_2))
print(parkinglot.park(vehicle_3))s
print(parkinglot.unpark(vehicle_1))
print(parkinglot.availability())