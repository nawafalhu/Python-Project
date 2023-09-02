def Prime(number) :
    for n in range(2, number) :
        if number % n == 0 :
            return print(f"{number} it's not a Prime number")
            
    print(f"{number} it's a Prime number")

n = int(input("Check this number: "))
Prime(n)