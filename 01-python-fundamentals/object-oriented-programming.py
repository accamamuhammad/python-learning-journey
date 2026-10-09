# object = A bundle of related attributes (variables) and methods (functions)
# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f'You drive the {self.model}')

    def stop(self):
        print(f'You stop the {self.model}')

car1 = Car('Mustang', 2018, 'red', False)
car2 = Car('M5', 2025, 'white', True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()
