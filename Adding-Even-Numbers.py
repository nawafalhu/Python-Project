sum = 0
for x in range(1, 101) :
    if x % 2 == 0 :
        sum += x

print(sum)

# or 

sum = 0
for x in range(0, 101, 2) :
    sum += x

# or

for x in range(0, 101, 2) :
    print(x)