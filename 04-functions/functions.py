# function = a block of re usable code

# Positional arguments
def birthday(name, age):
    print(f'Happy birthday {name}!')
    print(f'You are {age} now!')
 
birthday('Alamin', 21)

def display_invoic(username, amount, due_date):
    print(f'Hello {username}')
    print(f'your bill of ${amount:.2f} os due: {due_date}')

display_invoic('Alamin', 50, '01/06')

# Default arguments
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0.1))

# Keyword arguments
def hello(greeting, title, first, last):
    print(f'{greeting} {title}.{first} {last}')

hello(greeting='Hello', title='Mr', first='Eugine', last='Krabs')

# Arbitrary arguments (*args, **kwargs)
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2))

def display_name(*args):
    for arg in args:
        print(arg, end=' ')

display_name('Muhammad', "Hussaini", "Accama")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

print_address(street='kinshasa',
              city='abuja',
              state='FCT',
              zip='90853')

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label(
    'Dr.', 'Eugine', 'Krabbs',
    street='123 Alx St.',
    state='fct',
    city='ABJ',
    zip=25925)
