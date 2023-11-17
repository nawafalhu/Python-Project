
try:
    x = int(input('Please enter the value of x: '))
    y = int(input('Please enter the value of y: '))
    print(f'{x} divided by {y} = {x / y}')
except ZeroDivisionError :
    print("division by zero is undefined")
except ValueError : 
    print('only number')




