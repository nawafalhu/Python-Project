#import panda as pd
import csv


def KSU_Student(csvfile, Student_gender, Student_college, Student_degree):
    total_student = 0
    Student_gender = "ذكر"
    Student_college = "الأمير سلطان بن عبدالعزيز للخدمات الطبية الطارئة"
    Student_degree = "البكالوريوس"
    with open(r"D:\Python-Project\Uni\Lab07\Tweets\KSU.csv", 'r') as f :
        lines = csv.reader(f,delimiter=";")

        for row in lines :
            gender = row[0]
            college = row[1]
            degree = row[2]
            if degree == Student_degree and college == Student_college and gender == Student_gender:
                        total_student += 1
    return total_student

