# User Input

## Accepting user input
name = input('Enter your name: ')
age = int(input('Enter your age: '))
age = age + 1

print(f'Hello nigga {name}')
print(f'Your are {age} years old')

## madlibs game - exercise 1
place = input('Guess the place: ')
car = input('Guess the car: ')
person = input("Guess the last person: ")

print(f'Today i killed a nigga in {place}')
print(f'in the {place} i saw red {car}')
print(f'joe, kevin & {person} were there singing')

## calculate area of a rectangle - exercise 2
length = int(input('Enter the length of the rectangle: '))
breath = int(input('Enter the breath of the rectangle: '))

area = length * breath

print(f'The area of the rectangle is {area}')

## shooping cart program - exercise 3
item = input('What do you want to buy: ')
price =  float(input('What is the price: '))
quantity = int(input('How many?: '))

total = price * quantity

print(f'you have bought {quantity} x {item} the total is {round(total, 2)}')
