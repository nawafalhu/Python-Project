<<<<<<< HEAD

def write_file(file_name) :
    record = int(input("How many employee record you would like to save? "))
    with open(file_name, 'w') as file :

        for _ in range(0,record):
            name = input("Enter the employee's name: ")
            department = input("Enter the employee's department: ")
            salary = input("Enter the employee's salary: ")


            file.write(f"{name}, {department}, {salary}"+'\n')

# B

def delete_reecord(file_name, record_number) :
    with open(file_name, "r") as readfile :
        lines = readfile.readlines()
    del lines[record_number]

    with open(file_name, 'w') as writefile :
        for line in lines :        
            writefile.write(line)

=======

def write_file(file_name) :
    record = int(input("How many employee record you would like to save? "))
    with open(file_name, 'w') as file :

        for _ in range(0,record):
            name = input("Enter the employee's name: ")
            department = input("Enter the employee's department: ")
            salary = input("Enter the employee's salary: ")


            file.write(f"{name}, {department}, {salary}"+'\n')

# B

def delete_reecord(file_name, record_number) :
    with open(file_name, "r") as readfile :
        lines = readfile.readlines()
    del lines[record_number]

    with open(file_name, 'w') as writefile :
        for line in lines :        
            writefile.write(line)

>>>>>>> 40b695b7b8c1e383f5e04d5a00bb5c0d7e5c5353
# r'D:\Python-Project\Uni\Lab04\'