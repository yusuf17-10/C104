import csv

with open("Height.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

height_data=[]

for i in range(len(file_data)):
    num=file_data[i][1]
    height_data.append(float(num))

n=len(height_data)

height_data.sort()
if (n % 2==0):
    median1=float(height_data[n//2])
    median2=float(height_data[n//2-1])
    median=(median1+median2/2)
else:
    median=float(height_data[n//2])

print(median)