<<<<<<< HEAD
x = 4
for i in range(0, 3):
    for j in range(0, x):
        print(end=" ")
    x -= 1
    for j in range(0, i + 1):
        print("*", end=' ') 
    print("")
=======
row = 4
col = 3

for line in range(1,row):
    for space_in_the_beginning in range(col - line):
        print(' ',
              end='')  # This is to put spaces in each row depending on the row so first row has the most spaces and the last row has the fewest
    for stars_and_empty_space in range(line):
        print('*', end=' ')  # This is to draw the stars notice the space gap in the end of each star
    print()
>>>>>>> 28147f1 (added new small project)
