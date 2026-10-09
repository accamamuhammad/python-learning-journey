# collection = single 'variable' used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ['mango', 'apple', 'mango', 'bannana']

for fruit in fruits:
    print(fruit)
    
   
# check if in list
print('apple' in fruits)

# re-assign 
fruits[0] = ''

# add element
fruits.append('watermaleon')

# remove element
fruits.remove('appple')

# insert at an index
fruits.insert(0, 'pineapple')

# sort alphabetically
fruits.sort()

# clear list
fruits.clear()

# sets are just unordered lists
fruits = {'mango', 'apple', 'pineapple', 'bannana'}

# faster versions of lists
fruits = ('mango', 'apple', 'pineapple', 'bannana')

# Shopping cart program
# list, set & tupple - Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input('Enter food: (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter the price of a {food}: $: '))
        foods.append(food)
        prices.append(price)

print('----- YOU CART -----')

for food in foods:
    print(food, end=' ')

for price in prices:
    total += price
    print(total)
