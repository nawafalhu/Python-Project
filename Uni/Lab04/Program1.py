# s1 = ['100','Ali', 'null','IS', 'null']
# s2 = ['200','Ahmed','2.5','CS', 'null']
# s3 = ['300','Khalid','3.9','IS','undergrad']
# s4 = ['400','Nasser', 'null','SE','grad']
# s5 = ['500','Jamal','4.5','CS', 'null']

# file = open(r'D:\Python-Project\Uni\Lab04\Student_record.csv', 'w')
# file.write(s1[0]+' '+s1[1]+' '+s1[2]+' '+s1[3]+' '+s1[4]+'\n')
# file.write(s2[0]+' '+s2[1]+' '+s2[2]+' '+s2[3]+' '+s2[4]+'\n')
# file.write(s3[0]+' '+s3[1]+' '+s3[2]+' '+s3[3]+' '+s3[4]+'\n')
# file.write(s4[0]+' '+s4[1]+' '+s4[2]+' '+s4[3]+' '+s4[4]+'\n')
# file.write(s5[0]+' '+s5[1]+' '+s5[2]+' '+s5[3]+' '+s5[4]+'\n')
# file.close()


def convertStringToBytes(x):
    return bytes(x, "ascii") # Other Encoders
def convertBytestoString(x):
    return x.decode("ascii")
def convertIntTo4Bytes(x):
    return x.to_bytes(4, 'little')
def convert4BytesToInt(x):
    return int.from_bytes(x,"little")


def writeRecord(y,index):
    f = open("students.txt", "ab")
    position = f.tell()
    index[y[0]] = position
    l=convertIntTo4Bytes(len(y))
    f.write(l)
    for x in y:
        dataInBytes = convertStringToBytes(x)
        sizeInBytes = convertIntTo4Bytes(len(dataInBytes))
        f.write(sizeInBytes)
        f.write(dataInBytes)
    f.close()


s1 = ['100','Ali','4.5','IS']
s2 = ['200','Ahmed','2.5','CS']
s3 = ['300','Khalid','3.9','IS']
s4 = ['400','Nasser','3.8','SE']
s5 = ['500','Jamal','4.5','CS']
listOfStudents=[s1,s2,s3,s4,s5]
index = dict()
for y in listOfStudents:
    writeRecord(y,index)


def readRandomRecord(position):
    f = open("students.txt", "rb")
    f.seek(position)
    recordInfo = ''
    lenth=convert4BytesToInt(f.read(4))
    for _ in range(lenth):
        x = convert4BytesToInt(f.read(4))
        recordInfo += convertBytestoString(f.read(x))+","
    f.close()
    print(recordInfo)