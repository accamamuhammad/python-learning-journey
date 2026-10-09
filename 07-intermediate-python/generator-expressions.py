# Generator Expressions

number = int(input('Enter a number to count up to: '))

counter = (count for count in range(1, number + 1))

for n in counter:
    print(n)
