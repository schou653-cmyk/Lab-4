from classes1 import Team, Driver
# your code here

with open('f1_points.csv', 'r') as file:
    next(file)
    
    for line in file:
        data = line.split(',')
        driver = Driver(data[0], int(data[2]))