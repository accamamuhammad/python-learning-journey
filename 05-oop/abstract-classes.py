# Abstract Class
# A class that cannot be instantiated on its own; Meant to be subclassed.
# They can contain abstract methods, which are declared but have no implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @classmethod
    @abstractmethod
    def go(self):
        pass

    @classmethod
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print('Drive the Car')

    def stop(self):
        print('Stop the Car')

class Motocycle(Vehicle):
    def ride(self):
        print('Ride the Motocycle')

car = Car()

car.go()
car.stop()
