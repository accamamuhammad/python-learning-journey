# Iterators & Generators

import random

# Iterators Protocol: __iter__ and __next__
class MyIterator:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration

        current = self.number
        self.number -= 1
        return current

iterator = MyIterator(5)
for number in iterator:
    print(number)

class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.rolls:
            self.count += 1
            return random.randint(1, 6)
        else:
            raise StopIteration

dice_rolls = [die for die in Dice(3)]
print(dice_rolls)

# Generator Functions (yield)
def count_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

number = int(input('Enter a number to count to: '))
for n in count_to(number):
    print(n)

def read_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()
