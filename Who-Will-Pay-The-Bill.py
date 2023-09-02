import random

# names input from user
input_name = input("Give me everybody's names, separated by a comma.\n")

# split the name and save it in the names list
names = input_name.split(',')

# that choice random name from names list
random = random.choice(names)

# print the name
print(f"{random} is going to buy the meal today!")