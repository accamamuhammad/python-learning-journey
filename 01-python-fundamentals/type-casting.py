# Type Casting
## proces of converting value of one data type to another
## very import for managin user inputs and multiple other thigns

# Data
name = 'Alamin'
age = 22
cgpa = 4.01
engineer = True

## check type
# print(type(name))

# Explicit Type Casting
# convert age (int) to float
age = float(age)
print(age)

# convert cpga (float) to int
cgpa = int(cgpa)
print(cgpa)

# conver engineer (boolean) into a string
engineer = str(engineer)
print(engineer)

# convert age (int) to boolean
age = bool(age)
print(age)
## it will be false only if the number is zero otherwise its true
## can be used i forms when user does not input somehting in the field

# Implicit Type Casting
x = 1
y = 2.0
x = x/y
print(x)
## it changes to int when an operation was done on it
