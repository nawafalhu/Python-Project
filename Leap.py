# user input
year = int(input('Which year do you want to check?\n'))

# to check it's a leap or not
if float(year % 4) == 0 :
    if float(year % 100) == 0 :
        if float(year % 400) == 0 :
            print('Leap year.')
        else : 
            print("It is not Leap year.")
    else : 
        print("Leap year.")
else : 
    print("It is not Leap year.")