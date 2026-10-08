from classes1 import Team, Driver

# your code here

with open('f1_points.csv', 'r') as file:
    for line in file:
        data = line.split(',')

print(data)

