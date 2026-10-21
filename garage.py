
from models import car


class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def show_all(self):
        return self.vehicles

    def find_by_brand(self, brand):
        return [vehicle for vehicle in self.vehicles if vehicle.brand == brand]