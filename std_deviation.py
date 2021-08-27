import math
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

new_data = file_data[0]

def mean(data):
    print("Calculating mean value")
    n = len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total/n
    print("Average is = ", mean)
    return mean

#squaring and getting the values
squared_list = []
for number in new_data:
    a = int(number) - mean(new_data)
    print(a)
    a = a**2
    squared_list.append(a)
print(squared_list)
#getting_sum
sum = 0
for i in squared_list:
    sum = sum + i
print(sum)

#dividing the sum by the total values
result = sum/(len(new_data)-1)
print(result)

#getting the deviation by square root of the result
standard_deviation = math.sqrt(result)
print(standard_deviation)