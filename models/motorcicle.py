from models.vehicle import Vehicle  

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}), Has Sidecar: {self.has_sidecar}"

    def move(self):
        print(f"The motorcycle {self.brand} {self.model} is moving.")