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
total=0
for t in height_data:
    total=total+t
mean=total/n
print("mean  :"+str(mean))