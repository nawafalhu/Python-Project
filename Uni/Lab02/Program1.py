cost_list = []
cost = int(input("Enter the cost : (-1 to stop) $")) 
while cost != -1 :
    cost_list.append(cost)
    cost = int(input("Enter the cost : (-1 to stop) $")) 
print(cost_list)

length = len(cost_list)
print(f"The length of the list is {length}")

cost_tuple = tuple(cost_list)
print(cost_tuple)

# the highest value in the list
max = cost_list[0]
for item in cost_list :
    if item > max :
        max = item
print(f"The highest value in the list is {max}")

# the lower value in the list
min = cost_list[0]
for item in cost_list :
    if item < min :
        min = item
print(f"The lower value in the list is {min}")

# sum of all value in the list
sum = 0
for item in cost_list :
    sum += item
print(f"The sum of the list is {sum}")

# avg of the value
n = 0
for item in cost_list :
    sum += item
    n += 1
avg = sum // n
print(f"The avg of the list is {avg}")

# change the value of index 3 to 45

cost_list[3] = 45

# Remove the fourth cost in the list - display after and before
print(cost_list)
cost_list.pop(3)
print(cost_list)

# Remove 100 and print massege if doesn't exist
def Remove_100(thelist) :
    for item in thelist :
        if item == 100 : 
            return thelist.remove(item)
    print("doesn't exist")


Remove_100(cost_list)
print(cost_list)

    