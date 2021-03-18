import csv
from collections import Counter

with open("Height.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

height_data=[]

for i in range(len(file_data)):
    num=file_data[i][1]
    height_data.append(float(num))

data=Counter(height_data)
mode_data={
    "50-60":0,"60-70":0,"70-80":0
}
for height,occuarance in data.items():
    if(50<float(height)<60):
        mode_data["50-60"]+=occuarance
    elif(60<float(height)<70):
        mode_data["60-70"]+=occuarance
    elif(70<float(height)<80):
        mode_data["70-80"]+=occuarance




print(mode_data)
