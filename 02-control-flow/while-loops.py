# While Loop

# Example 1 
name = input('Enter you name: ')

while name == '':
    print('You did not enter your name')
    name = input('Enter you name: ')
print(f'Hello {name}')

# Example 2
age = int(input('Enter you age: '))

while age < 0:
    print("Age can't be negative")
    age = int(input('Enter your age: '))

print(f'You are {age} yearls old')

# Example 3
food = input('Enter a food you like (q to quit): ')

while not food == 'q':
    print(f'you like {food}')
    food = input('Enter another food you like (q to quit): ')

print('bye')
