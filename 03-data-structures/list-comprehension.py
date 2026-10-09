# list comprehension = concise way to create lists in pyhton, compact and easier to read than traditional loops [expression for value in iterable if condition]

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

# use list compresion to make it more concise
doubles = [x * 2 for x in range(1, 11)]

fruits = ['apple', 'orange', 'bannna', 'coconut']
fruits = [fruit.upper() for fruit in fruits]

print(fruits)
