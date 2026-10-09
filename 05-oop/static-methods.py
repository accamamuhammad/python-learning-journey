# Static methods = Belong to a class rather than an instance; best for utility functions

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance method
    def get_info(self):
        return f'{self.name} is the {self.position}'

    # Static method
    @staticmethod
    def is_valid(position):
        valid_positions = ['chef', 'chashier', 'manager', 'janitor']
        return position in valid_positions

employee1 = Employee('master', 'manager')
employee2 = Employee('zadok', 'chef')
employee3 = Employee('shamo', 'janitor')
employee4 = Employee('zakadad', 'chashier')

print(Employee.is_valid('chef'))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())
