# class variables = Shared among all in instances of a class
# Defined outside the contructor
# Allow you to share data among all objects created from that class

class Student:
    # class variable (shared among all)
    class_year = 1999
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student('Krabs', 67)
student2 = Student('Sandy', 44)

print(Student.class_year)
print(student1.class_year)
print(student2.class_year)
