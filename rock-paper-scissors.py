import random as rd

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# input user
user = input("What do you choose? Rock, Paper, Scissors.\n").capitalize()

# computer choise
list = [rock, paper, scissors]
random = rd.choice(list)

# Rock section 
if user == "Rock" : 
    print(rock)
    print(f"Computer chose :\n{random}")
    if random == list[0] : 
        print("Try again")
    elif random == list[2] : 
        print("You win!")
    else : 
        print("You lose")

# Paper section
elif user == "Paper" : 
    print(paper)
    print(f"Computer chose :\n{random}")
    if random == list[1] : 
        print("Try again")
    elif random == list[0] : 
        print("You win!")
    else : 
        print("You lose")
 # Scissors section
elif user == "Scissors" : 
    print(scissors)
    print(f"Computer chose :\n{random}")
    if random == list[2] : 
        print("Try again")
    elif random == list[1] : 
        print("You win!")
    else : 
        print("You lose")
else : 
    print("Wrong! Try again")