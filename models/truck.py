from models.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}), Max Load: {self.max_load} kg"

    def move(self):
        print(f"The truck {self.brand} {self.model} is moving.")