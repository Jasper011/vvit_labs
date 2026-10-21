from models.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}), Doors: {self.doors}"

    def move(self):
        print(f"The car {self.brand} {self.model} is moving.")