# Nested class = A class defined within another class
# Encapsulates details not relevant outside the outer class and keeps the namespace clean

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f'{self.name} {self.position}'

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employee(self):
        for employee in self.employees:
            print(f'{employee.name} The {employee.position}')

company1 = Company('Yaba Autos')
company2 = Company('Jack Logs')

company1.add_employee('Yaba Lex', 'Manager')
company1.add_employee('Accama YK', 'Chairman')
company1.add_employee('Auti Autos', 'Middleman')

company2.add_employee('Omo Lex', 'Senior')
company2.add_employee('Guy YK', 'Guy affairs')
company2.add_employee('Manster', 'Card Holder')

print('Company 1')
company1.list_employee()

print('\nCompany 2')
company2.list_employee()
