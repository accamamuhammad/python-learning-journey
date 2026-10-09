# Composition = The composed object directly owns its components, which cannot exist independently ("owns-a" relationship)

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f'{self.make} {self.model} with {self.engine.horse_power} HP and rim size of {self.wheels[0].size}'

car = Car(make='Bmw', model='M5', horse_power=777, wheel_size=21)

print(car.display_car())
