x = 4
for i in range(0, 3):
    for j in range(0, x):
        print(end=" ")
    x -= 1
    for j in range(0, i + 1):
        print("*", end=' ')
    print("")