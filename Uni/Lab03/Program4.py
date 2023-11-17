<<<<<<< HEAD

# Slow program
def slow_one() :
    n=0
    All_Student_ID=[123,324,231,1233,33,4,345,32,4,32]
    All_Student_ID.sort()
    Student_ID = []
    Student_ID.append(All_Student_ID[0])
    for id in range(1, (len(All_Student_ID)-1)) :
            pre_id = All_Student_ID[n]
            curr_id = All_Student_ID[id]
            if curr_id != pre_id :
                Student_ID.append(curr_id)
            n+=1
    return Student_ID


# Fast Program
def Fast_one() :
     Student_ID = set([12,345,67,345,12])
     return Student_ID



=======

# Slow program
def slow_one() :
    n=0
    All_Student_ID=[123,324,231,1233,33,4,345,32,4,32]
    All_Student_ID.sort()
    Student_ID = []
    Student_ID.append(All_Student_ID[0])
    for id in range(1, (len(All_Student_ID)-1)) :
            pre_id = All_Student_ID[n]
            curr_id = All_Student_ID[id]
            if curr_id != pre_id :
                Student_ID.append(curr_id)
            n+=1
    return Student_ID


# Fast Program
def Fast_one() :
     Student_ID = set([12,345,67,345,12])
     return Student_ID



>>>>>>> 40b695b7b8c1e383f5e04d5a00bb5c0d7e5c5353
