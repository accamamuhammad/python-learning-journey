# Data Class = A special kind of class designed mostly for holding data (Python 3.7+)
# Automatically generates: __init__, __repr__, __eq__

from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    password: str = field(repr=False)
    is_alive: bool = True

    def __post_init__(self):
        if self.age < 0:
            raise ValueError('Age cannot be negative')

person1 = Person('Alamin', 22, '1234')
person2 = Person('Spongebob', 22, 'madoo')

print(person1)
print(person2)
