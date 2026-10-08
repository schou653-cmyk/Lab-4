from classes1 import Team, Driver
# your code here

teams = {}

with open('f1_points.csv', 'r') as file:
    next(file)

    for line in file:
        data = line.split(',')

        driver = Driver(data[0], int(data[2]))
        team_name = data[1]

        if team_name not in teams:
            teams[team_name] = Team(team_name)

        teams[team_name].add_driver(driver)

print(teams)