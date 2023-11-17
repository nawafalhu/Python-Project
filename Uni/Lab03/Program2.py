<<<<<<< HEAD
original_dict = {'English' : [83, 74, 90], 'Biology' : [86, 89, 92], 'Math' : [74, 84, 91]}

# def update_dict(dic, sub) :
#     list = []
#     for value in dic[sub] :
#         list.append(value + 5)
#     dic[sub] = list
#     return dic

# print(update_dict(original_dict, 'Biology'))

n = 0
for value in original_dict['Biology'] :
    original_dict['Biology'][n] = value + 5
    n+=1
print(original_dict)

=======
original_dict = {'English' : [83, 74, 90], 'Biology' : [86, 89, 92], 'Math' : [74, 84, 91]}

# def update_dict(dic, sub) :
#     list = []
#     for value in dic[sub] :
#         list.append(value + 5)
#     dic[sub] = list
#     return dic

# print(update_dict(original_dict, 'Biology'))

n = 0
for value in original_dict['Biology'] :
    original_dict['Biology'][n] = value + 5
    n+=1
print(original_dict)

>>>>>>> 40b695b7b8c1e383f5e04d5a00bb5c0d7e5c5353
