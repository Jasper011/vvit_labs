
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__speed = 0

    @abstractmethod
    def move(self):
        pass

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}), Speed: {self.speed} km/h"

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной.")
        self.__speed = value

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement

    def stop(self):
        self.speed = 0

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})"
    