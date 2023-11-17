<<<<<<< HEAD
header = ['Student_Name', 'IS240', 'IS230', 'IS111', 'IS113']

student_list={
    'Header' : ['Student Name','IS240','IS230' ,'IS111', 'IS113'],
    'Ali': ['15', '12', '10', '13'],
    'Mohammed':['11','14','12','8'],
    'Nasser': ['9','15','11','7']
}

# with open('Student2.csv', 'w') as student :
#     fieldname=student_list[0].keys()
#     student.writelines(fieldname)
#     for n in range(0,len(student_list) - 1) :
#         student.write(student_list[n].values())

# def Write_CSV(CSVFile) :
#     file = open(CSVFile, 'w')
#     file.write



with open(r'D:\Python-Project\Uni\Lab04\student.csv', "w") as file:
    # Write the header row.
    header = student_list["Header"]
    header_string = ",".join(header)
    file.write(header_string + '\n')
    for name, marks in student_list.items():
      if name != 'Header' :
        row_string = name+','+ ",".join(marks)
=======
header = ['Student_Name', 'IS240', 'IS230', 'IS111', 'IS113']

student_list={
    'Header' : ['Student Name','IS240','IS230' ,'IS111', 'IS113'],
    'Ali': ['15', '12', '10', '13'],
    'Mohammed':['11','14','12','8'],
    'Nasser': ['9','15','11','7']
}

# with open('Student2.csv', 'w') as student :
#     fieldname=student_list[0].keys()
#     student.writelines(fieldname)
#     for n in range(0,len(student_list) - 1) :
#         student.write(student_list[n].values())

# def Write_CSV(CSVFile) :
#     file = open(CSVFile, 'w')
#     file.write



with open(r'D:\Python-Project\Uni\Lab04\student.csv', "w") as file:
    # Write the header row.
    header = student_list["Header"]
    header_string = ",".join(header)
    file.write(header_string + '\n')
    for name, marks in student_list.items():
      if name != 'Header' :
        row_string = name+','+ ",".join(marks)
>>>>>>> 40b695b7b8c1e383f5e04d5a00bb5c0d7e5c5353
        file.write(row_string + "\n")