# Love calculator - https://app.codingrooms.com/management/assignments/364926/overview 37. 5:00

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

All_name = name1 + name2
t = All_name.count("t")
r = All_name.count("r")
u = All_name.count("u")
e = All_name.count("e")

l = All_name.count("l")
o = All_name.count("o")
v = All_name.count("v")
e = All_name.count("e")

total_score = t + r + u + e + l + o + v + e

if total_score < 10 or total_score > 90 :
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50 :
    print(f"Your score is {total_score}, you are alright together.")
else : 
    print(f"Your score is {total_score}.")