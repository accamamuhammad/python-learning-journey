# For loops

## loops for a fixed number of times

# to loop 10 times
for x in range(1, 11):
    print(x)
    
# count backwards
for x in reversed(range(1, 11)):
    print(x)

print('HAPPY EID')

#iterate over a string
credit_card = '1234-5678-1456'

for x in credit_card:
    print(x)
    
    
# continue 
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
        
# break   
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
