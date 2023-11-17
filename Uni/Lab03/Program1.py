<<<<<<< HEAD
Social_Network = {
    "Ahmed" : {"Khalid", "Nora"},
    "Ali" : {"Khalid", "Nora", "Fahad"},
    "Lela" : {"Fahad", "Sara"},
    "Fahad" : {"Khalid", "Lela", "Ali"},
    "Khalid" : {"Fahad", "Ali", "Ahmed"},
    "Nora" : {"Sara", "Ahmed", "Ali"},
    "Sara" : {"Ali", "Lela", "Nora"}
}


# Added user without any friende
def New_User(x) :
    if x not in Social_Network :
        Social_Network[x] = {}
    return Social_Network

# return how many friend that user have 
def User_Frindes(x) :
    friendes = Social_Network.get(x, "No user with this name")
    return friendes

# add x to y as a friend and y to x as friend
def added_User_With_Friendes(x,y):
    if x not in Social_Network and y not in Social_Network :
        Social_Network[x] = y 
        Social_Network[y] = x 
    return Social_Network

# remove x from y and y from x 
def remove_friends(x,y) :
    if x in Social_Network and y in Social_Network :
        Social_Network[x].remove(y)
        Social_Network[y].remove(x)
    else :
        print("User x and y does not exists")        
    return Social_Network
=======
Social_Network = {
    "Ahmed" : {"Khalid", "Nora"},
    "Ali" : {"Khalid", "Nora", "Fahad"},
    "Lela" : {"Fahad", "Sara"},
    "Fahad" : {"Khalid", "Lela", "Ali"},
    "Khalid" : {"Fahad", "Ali", "Ahmed"},
    "Nora" : {"Sara", "Ahmed", "Ali"},
    "Sara" : {"Ali", "Lela", "Nora"}
}


# Added user without any friende
def New_User(x) :
    if x not in Social_Network :
        Social_Network[x] = {}
    return Social_Network

# return how many friend that user have 
def User_Frindes(x) :
    friendes = Social_Network.get(x, "No user with this name")
    return friendes

# add x to y as a friend and y to x as friend
def added_User_With_Friendes(x,y):
    if x not in Social_Network and y not in Social_Network :
        Social_Network[x] = y 
        Social_Network[y] = x 
    return Social_Network

# remove x from y and y from x 
def remove_friends(x,y) :
    if x in Social_Network and y in Social_Network :
        Social_Network[x].remove(y)
        Social_Network[y].remove(x)
    else :
        print("User x and y does not exists")        
    return Social_Network
>>>>>>> 40b695b7b8c1e383f5e04d5a00bb5c0d7e5c5353
