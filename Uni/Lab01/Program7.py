n = int(input("Please enter a number:\n"))

num=1
for n in range(1, n + 1):
    num *= n 

print(f"Factorial of {n} == {num}")