<<<<<<< HEAD
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
=======
def prime(n):
    # check if the number less than 0
    if n < 0:
        print('Please enter positive numbers only!')
        exit()
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
>>>>>>> 28147f1 (added new small project)
