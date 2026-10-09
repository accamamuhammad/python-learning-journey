# format specifiers = {value:flags} formar a value based on what flag is inserted

# • (number)f = round to that many decimal places (fixed point)|
# : (number) = allocate that many spaces
# : 03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# i = insert a space before positive numbers
# :, = comma separator

price1 = 3.1459355 
price2 = 61.244
price3 = -99.14

# display 2 decimal places and floar
print(f'price 1 is ${price1:.2f}')
print(f'price 2 is ${price2:.2f}')
print(f'price 3 is ${price3:.2f}')
