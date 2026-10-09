# Class methods = Operations related to the class itself (takes `cls` as first parameter)

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f'{self.name} - {self.gpa}'

    @staticmethod
    def gpa_grading(gpa):
        if gpa < 3:
            return '3rd Class'
        elif gpa > 3 and gpa < 4.5:
            return '2nd class'
        else:
            return '1st class'

    @classmethod
    def get_count(cls):
        return f'Total Number of students: {cls.count}'

    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f'The average gpa is: {cls.total_gpa / cls.count}'

student1 = Student('Alamin', 4.5)
student2 = Student('Shamo', 2.5)
student3 = Student('Yakson', 5.0)
student4 = Student('Tony', 3.3)

print(Student.get_count())
print(Student.average_gpa())

print(Student.gpa_grading(student1.gpa))
print(Student.gpa_grading(student2.gpa))
print(Student.gpa_grading(student3.gpa))
print(Student.gpa_grading(student4.gpa))
