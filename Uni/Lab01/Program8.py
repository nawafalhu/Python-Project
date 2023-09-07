number = int(input("Enter numbers to calculate their sum and average. Enter 0 to exit:\n"))

sum = 0
count = 0 
while number != 0 :
    count += 1
    sum = sum + number
    avg = sum // count
    print(f"Sum = {sum}, Average = {avg}")
    number = int(input("Enter numbers to calculate their sum and average. Enter 0 to exit:\n"))