
class Driver:

    def __init__(self, name: str, points: int):

        self.name = name
        self.points = points
        pass # your code here

    def __repr__(self) -> str:
        """
        This method defines what the human-readable string version of the Driver object is.
        It should return a string that describes this Driver. For example:
        "Carlos Sainz (200 pts)"
        """
        return f'{self.name} has {self.points}'
        
        pass # your code here


class Team:

    def __init__(self, name: str):
        """
        :param name: the team's name
        """
        self.name = name
        self.drivers = []
        pass # your code here

    def add_driver(self, driver: Driver) -> None:
        """
        adds a Driver to this team (by appending it to self.drivers)
        :param driver: the Driver object to add to this Team
        """

        self.drivers.append(driver)


        pass # your code here

    def get_total_points(self) -> int:
        """
        :return: sum of points scored by this team's Drivers
        """
        total = 0

        for driver in self.drivers:
            total += driver.points

        return total

        pass # your code here

    def __repr__(self) -> str:
        """
        This method defines what the human-readable string version of the Team object is.
        It should return a string that describes this Team, for example:
        "FERRARI with drivers Carlos Sainz, Charles Leclerc. Total pts: 406"
        """

        names =''

        for driver in self.drivers:
            names += driver.name + ' , ' 

        return f'{self.name} with {names}. Total point: ({self.get_total_points()})'
        pass # your code here
    
    def __lt__(self, other) -> bool:
        """
        This method defines what "less than" means for the Team object
        It should return True if this Team (self) is "less than" another.
        In this case, it should return True if this team has less total points that the other.
        :param other: another Team object
        :return: True if this Team has less points than other
        """
        self.other = other

        other.get_total_points()

        return self.get_total_points() < other.get_total_points()

        

        pass # your code here
