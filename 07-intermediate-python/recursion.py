# Recursion = Function calling itself until it reaches a base condition

# Example 1: Walking steps
def walk(steps):
    if steps == 0:
        return
    print(f'You take step #{steps}')
    walk(steps - 1)

walk(100)

# Example 2: Factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(10))
