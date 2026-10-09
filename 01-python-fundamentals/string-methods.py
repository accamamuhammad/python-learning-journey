# String Methods

name = input('Enter your full name: ')
number = input('Enter your phone number: ')

# Get length of a string
result1 = len(name)

# Find first occurance of a letter
result2 = name.find('a')

# Find last occurance of a letter
result3 = name.rfind('a')

# Capitalize
result4 = name.capitalize()

# Upper Case
result5 = name.upper()

# Lower Case
result6 = name.lower()

# check if string has all digits
result7 = name.isdigit()

# check if string has only alphabetical letters
result7 = name.isalpha()thow 

# count number of characters in a string
result8 = number.count('-')

# replace any occurance
result9 = number.replace('-', "")

# Excersie 1 - validate user input
# Rules
# 1. username < 12 characters
# 2. username = no spaces
# 3. username = no digits

name = input('Enter a username: ')
password = int(input('Enter a password: '))

# remove spaces from username lenght of username
no_space = name.replace(" ", "")

# check length of username
character = len(no_space)

# check for digits
digits = name.isalpha()


# validation logic

if character > 12 and not digits:
    print('username must be less than 12 characters & no numbers')
elif character > 12:
    print('username must be less than 12 characters')
elif not digits:
    print('username should not contain numbers')
else:
    print(f'Success: ')
    print(f'Username: {no_space}')
    print(f'Success: {password}')
