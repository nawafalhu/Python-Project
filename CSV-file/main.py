# old way
# with open(r"D:\Python-Project\CSV-file\weather_data.csv") as csv :
#     data = csv.readlines()
#     print(data)

import csv 

tempr = []
with open(r"D:\Python-Project\CSV-file\weather_data.csv") as file :
    data = csv.reader(file)
    for row in data :
        if row[1] != 'temp' :
            tempr.append(int(row[1]))
    print(tempr)

import pandas as pd

data = pd.read_csv(r"D:\Python-Project\CSV-file\weather_data.csv")
temp_list = data['temp'].to_list()
print(temp_list)
avg = sum(temp_list) // len(temp_list)
print(avg)
print(data['temp'].max())
