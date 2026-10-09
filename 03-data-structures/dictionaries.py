# Dictionary = collect of {key:value} pairs ordered and changable. No duplicates

capitals = {'Nigeria': 'Lagos',
            'Kenya': 'Nairobi',
            'Japan': 'Tokyo',
            'Uk': 'london'}

# get a specific key
print(capitals.get('Nigeria'))

# update existing or add new
capitals.update({'Germany': 'Berlin'})
capitals.update({'Nigeria': 'Abuja'})

# return keys
keys = capitals.keys()

# values of the keys
values = capitals.values()

items = capitals.items()

print(items)
