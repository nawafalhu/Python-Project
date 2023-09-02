userinp = 0 
while userinp != "E" :
    userinp = input("to convert the temperature from C to F (Press F) \nto convert the temperature from F to C (Press C) \nto End the program (Press E) \nEnter your choice : ").capitalize()
    # to convert from F to C
    if userinp == "C" :
        Ftemp = int(input("Enter the temperature in Fehrenheit is : "))
        C = round(((Ftemp - 32) * 5/9), 1)
        
        if Ftemp > 30 :
            print("it's a sunny day")
        elif Ftemp < 30 :
            print("it's a cold day")
        print("the temperature in Celsius is : ", C)
    
    # to convert from C to F
    elif userinp == "F" : 
        Ctemp = int(input("Enter the temperature in Celsius : "))
        F = round((Ctemp * 1.8) + 32, 1)
        if Ctemp > 30 :
            print("it's a sunny day")
        elif Ctemp < 30 :
            print("it's a cold day")
        print(f"the temperature in Fahrenheit is : {F}")
    
    # to end the program
    elif userinp == "E" :
        break
    # if the user enter another value
    else : 
        print("Try agan")

print("Goodbye!")
