# Print the welcom massege
print("Welcome to Treasure Island. Your mission is to find the treasure.")

# Left or Right
RorL = input("left or right? ").lower()
if RorL == "right" :
    print("Fall into a hole.\nGame Over.")
    
else : 
    print("Right choice!")

# Swim or Wait
SorW = input("swim or wait? ").lower()
if SorW == "swim" :
    print("Attacked by trout.\nGame Over.")
else : 
    print("Right choice!")

# Which door 
door = input("Which door? Blue, Yellow, Red ").lower()
if door == "Blue" or door=="Red" :
    print("Game Over.")
else : 
    print("Right choice!")
