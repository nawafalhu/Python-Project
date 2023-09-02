import time as t
x = 5
while x > 0 :
    print(x)
    t.sleep(1)
    x -= 1

number = int(input("Enter the number: "))
x = 1
for z in range(1,number):
    x = x * number
    number -= 1
print(x)