# Compound Interest Calculator

# formula:
## A = P(1+r/100)*n
## principal_balance(1+interest_rate/100)**period

principal_balance = float(input('Enter the Principle Balance: '))
interest_rate = float(input('Enter the interest rate: '))
period = float(input('Enter period (years): '))

x = 0
interest_to_percentage = interest_rate/100
interest_plus_one = interest_to_percentage + 1

while not x == period:
    x += 1
    result = pow(interest_plus_one, period)
    final_amount = round(principal_balance * result, 2)
print(f'{final_amount:,}')
