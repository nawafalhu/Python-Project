def Prime(x) :
    num = 0
    for n in range(2, x) :
        if x % n == 0 :
            num = -1        
    if num == -1 :
        print(f"{x} is not a prime number")
    else : 
        print(f"{x} is a prime number") 
        

user = int(input("Please enter a number:\n"))
Prime(user)