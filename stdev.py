import csv
import math
import statistics

with open("data.csv",newline = "")as f:
    reader = csv.reader(f)
    filedata = list(reader)
data = filedata[0]
#mean
def mean(data):
    n=len(data)
    total =0
    for x in data:
        total +=int(x)
    mean = total /n
    return mean

#square
sqList =[]
for number in data :
    a = int(number)-mean(data)
    a = a**2 #a** power 2
    sqList.append(a)

# summing over square
sum =0
for i in sqList:
    sum = sum+1

#divide result with total values
result = sum / (len(data)-1)

standardDeviation = math.sqrt(result)
print(standardDeviation)


#inbuilt function for std
#print("inbuilt------",statistics.stdev(data))
