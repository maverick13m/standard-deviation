import csv
#calss 1
with open("class1.csv",newline = "")as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
totalMarks = 0
length = len(filedata)
for marks in filedata:
    totalMarks += float(marks[1])
mean = totalMarks/length
print("mean of class-1", mean)

#class 2
with open("class2.csv",newline = "")as f:
    reader2 = csv.reader(f)
    filedata2 = list(reader2)
filedata2.pop(0)
totalMarks2 = 0
length2 = len(filedata2)
for marks in filedata2:
    totalMarks2 += float(marks[1])
mean2 = totalMarks2/length2
print("mean of class-2", mean2)

import pandas as pd
import plotly.express as px

df = pd.read_csv ("class1.csv")
fig1 = px.scatter(df,x="Student Number",y="Marks")
fig1.update_layout(shapes =[dict(type="line",y0=mean,y1=mean,x0=0, x1=length)])
fig1.show()

df2 = pd.read_csv ("class2.csv")
fig2 = px.scatter(df2,x="Student Number",y="Marks")
fig2.update_layout(shapes =[dict(type="line",y0=mean2,y1=mean2,x0=0, x1=length2)])
fig2.show()






    