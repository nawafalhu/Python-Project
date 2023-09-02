import random as rd

mylist = ['Head', 'Tail']

print(rd.choice(mylist))

# or

random = rd.randint(0,1)
if random == 1 : 
    print('Head')
else :
    print('Tail')