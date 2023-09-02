row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]

# print the map
print(f"{row1}\n{row2}\n{row3}")

# input number from user 
position = input("Where do you want to put the treasure? ")

# to determine  the first and second number
horizonal = int(position[0])
vertical = int(position[1])

# replace the white square to X
map[vertical - 1][horizonal - 1] = " X"

# print the result
print(f"{row1}\n{row2}\n{row3}")

