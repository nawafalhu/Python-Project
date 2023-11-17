list = ['Blue color', 'Red#', 'Purple', 'Red %', 'Black']

<<<<<<< HEAD
special_char = '@_!#$%^&*()<>?/\|}{~:;.[]'
 
out_list = [''.join(x for x in string if not x in special_char) for string in list]

print(list)
print(out_list)
=======
special_char = ['%','color','#']

print(list)

filter_list=[]
for word in list:
    filtered_word = []
    x = word.split()
    for w in x:
        flag=False
        for fword in special_char:
            if w in fword:
                flag=True
                break 
        if flag==False:
            filtered_word.append(w)
    filter_list.append(" ".join(filtered_word))        
            
print(filter_list)



################### This is prefered solution to the table question #####################################
cells = "ABCDEF" # we will use this string to fill our table, since cells[0] = A, and so on.
rows = [] # this list will be the rows, lis[0] should contain [A,B,C] , lis[0][1] = B 
for row in range(2): # this loop will be responsible for the row construction , so in the first iteration will be constructing row 0 which is [A,B,C]
    columns=[] # this list will hold the columns values, but we will fill it, based on the row.
    for i in range(3): # i is the current column.
        current_letter_index= i+(3*row) # this step will decide what letter index we use from cells string based on the row. So if we are in row 0 and i(the column) is 0  we will choose index 0
                                        # since 0 + (3*0)=0 ;however if we are at row 1 and i(the column ) is 0 then we choose index 3 since 0 + (3*1) = 3.
        columns.append(cells[current_letter_index])  # this step returns append the apporpriate letter based on the currect letter index
    rows.append(columns) # this will add the columns list to the current row 
print(rows)
################### This is prefered solution to the table question #####################################




def remove_words1(string_list, remove_list):
    updated_list = [] # this will contain all of sentences after removing the wrong words for example this will contain ['Blue' , '','Purple', 'Red', 'Black'] and after we finish we return it

    for sentence in string_list: # This for loop will return the sentences in string_list e.g. blue color , Red# call this for-loop loop1

        splitted_word=sentence.split() # we split the word by the spaces  so blue color will become ['blue' , color] , and Red# will be ['Red#']

        list_of_updated_word=[] # this list will contain the word that are only valid in order to recreate a list that for example contain ['blue'] then we will use join to reconstruct the string.

        for w in splitted_word: # this for loop will go through the words that are spliited by space e g ['blue' , 'color'] , ['Red#'] call this for-loop loop2

             flag= False # this flag will tell us if the current word is valid or not

             for rword in remove_list:  # this for loop will go over all the porhibited words call this for-loop loop3

                 if rword in w: # check if the porhibited word exists in the current word

                     flag=True # if the porhibited word exists in the current word set the flag to True  

                     break # stop looping over the other porhibited words since one porhibited word is sufficient  

             if flag==False : # if we leave the loop3 and the flag is still false then add this word to a valid list which is called new string

                 list_of_updated_word.append(w) # for example now this list will contain ['blue'] on the first iteration of loop 2. the second iteration of loop 2 will detect the word color.

        updated_string = " ".join(list_of_updated_word)

        updated_list.append(updated_string)
    return updated_list
>>>>>>> 28147f1 (added new small project)
