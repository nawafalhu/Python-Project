age = int(input("Enter your age: "))

if age <= 25 and age >= 18 :
    print("your age is betwen 25 and 18")
elif age > 25 and age < 100 :
    print("your age is grater than 25")
elif age < 18 and age > 0:
    print("your age is less than 18")
else : 
    print("Please Enter a right age")
