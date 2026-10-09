# String indexing

## indexing = accesing elemnts of a sequence using [] (indexing operators) [start : end : step]

credit_number = '1234-5678-9102'

# starting position
print(credit_number[4])

# range position
print(credit_number[0:4])

# with step
print(credit_number[0:4:2])

# will print all second characters
print(credit_number[::2])

# last character, like from the back
print(credit_number[-14])

# String indexing - Excercise

email = input('Enter your email: ')

index = email.index('@')

username = email[:index]
domain = email[index + 1:]

print(f'Your username is {username} & domain is {domain}')
