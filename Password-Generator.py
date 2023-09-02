import random as rd
# The list of letters, number and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '?', '@', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letter= int(input("How many letters would you like in your password?\n")) 
num_symbol = int(input(f"How many symbols would you like?\n"))
num_number = int(input(f"How many numbers would you like?\n"))

password_list = []
for char in range(1, num_letter + 1):
    password_list.append(rd.choice(letters))

for char in range(1, num_number + 1):
    password_list.append(rd.choice(numbers))


for char in range(1, num_symbol + 1):
    password_list.append(rd.choice(symbols))

rd.shuffle(password_list)

password=""
for char in password_list :
    password += char

print(f"Your password is : {password}")