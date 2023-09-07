import random as rd

print("Welcom To The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

guess = rd.randint(1, 100)

def hard() : 
    number_of_guess = 5
    user_guess = None
    while  user_guess != guess and number_of_guess != 0 :
        user_guess = int(input("Make a guess: "))
        if user_guess > guess :
            print("Too heigh.\nGuess again")
        elif user_guess < guess : 
            print("Too low.\nGuess again")
        elif user_guess == guess :
            print("You win!")
            return
        number_of_guess -= 1
        print(f"You have {number_of_guess} attempts remaining to guess the number. ")
    print("You lose.")


def esay() : 
    number_of_guess = 10
    user_guess = None
    while  user_guess != guess and number_of_guess != 0 :
        number_of_guess -= 1
        user_guess = int(input("Make a guess: "))
        if user_guess > guess :
            print("Too heigh\nGuess again")
        elif user_guess < guess : 
            print("Too low.\nGuess again")
        elif user_guess == guess :
            print("You win!")
            return
        print(f"You have {number_of_guess} attempts remaining to guess the number. ")
    print("You lose.")


if level == "hard" : 
    hard()
elif level == "easy" :
    esay()   
    