from models.vehicle import Vehicle

class Boat(Vehicle):
    def __init__(self, brand, model, year, length, water_line):
        super().__init__(brand, model, year)
        self.length = length
        self.water_line = water_line

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}), Length: {self.length} meters, Water Line: {self.water_line} meters"

    def move(self):
        print(f"The boat {self.brand} {self.model} is sailing.")