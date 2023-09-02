import random as rd


lists = [1,2,3,4,5,6,7,8,9]
number = rd.choice(lists)
guess = None
number_of_guess = 10
print("Guess the number!")
while guess != number and number_of_guess != -1 : 
    guess = int(input("Is it... "))
    if guess == number:
        print("Wow! You guessed it right!")
    elif guess < number:
        print("Opps, It's bigger...")
        print(f"You only have {number_of_guess} Guesses!")
    elif guess > number:
        print("Opps, It's not so big.")
        print(f"You only have {number_of_guess} Guesses!")
    if guess == number and number_of_guess > 6 :
        print("You are an amazing guesser!")
        break
    number_of_guess -= 1
    if number_of_guess == -1 :
        print("Game over")
    
    