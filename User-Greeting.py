names = "nawaf"

name = input("what is your name? ")
age = int(input("how old are you? "))
if name == names :
    print(f"Welecom {name} to our program!")
else :
    print("wrong name")

if age <= 25 and age >= 18 :
    print("hello, young one!")
elif age > 25 and age < 100 :
    print("welcome !")
elif age < 18 and age > 0:
    print("sorry, your age is less than 18")
else : 
    print("Please Enter a right age")