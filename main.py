from models.car import Car
from models.truck import Truck
from models.motorcicle import Motorcycle
from models.boat import Boat
from garage import Garage

def main():
    yamaha = Motorcycle("Yamaha", "R1", 2026, False)
    tractor = Truck("John Deere", "X9", 2023, 1000)

    print(yamaha.brand, yamaha.model, yamaha.year)
    print(tractor.brand, tractor.model, tractor.year)  

    yamaha.accelerate(50)
    print(yamaha.speed)
    yamaha.brake(20)
    print(yamaha.speed)    
    yamaha.stop()
    print(yamaha.speed)
    print(yamaha.get_info())

    # yamaha.brake(10) 

    print(yamaha)
    yamaha.accelerate(100)
    print(yamaha)

    bmw_x5 = Car("BMW", "X5", 2022, 5)
    print(bmw_x5.get_info())
    bmw_x5.accelerate(80)
    print(bmw_x5.speed)
    bmw_x5.brake(30)
    print(bmw_x5.speed)
    bmw_x5.stop()
    print(bmw_x5.speed)

    # undefined_vehicle = Vehicle("Undefined", "Model", 2025)

    vehicles = [bmw_x5, yamaha, tractor]
    for vehicle in vehicles:
        vehicle.move()
        print(vehicle.get_info())

    vehicles.append(Car("Audi", "A4", 2021, 4))
    vehicles.append(Truck("Volvo", "FH16", 2020, 20000))
    vehicles.append(Motorcycle("Harley-Davidson", "Street 750", 2019, True))
    vehicles.append(Car("BMW", "3 Series", 2023, 4))
    vehicles.append(Truck("Mercedes-Benz", "Actros", 2022, 18000))
    vehicles.append(Boat("Yamaha", "242X", 2021, 8, 4.5))

    print('=' * 30)
    garage = Garage()
    for vehicle in vehicles:
        garage.add_vehicle(vehicle)

    for vehicle in garage.show_all():
        print(vehicle.get_info())
    print('=' * 30)
    for vehicle in garage.find_by_brand("BMW"):
        print(vehicle.get_info())

if __name__ == "__main__":
    main()