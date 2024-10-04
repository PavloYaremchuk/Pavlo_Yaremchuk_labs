from player import Player
from coach import Coach
from person import Person

class PlayingCoach(Player, Coach):
    def __init__(self, name, surname, age, nationality, number, position, average_points, experience, specialization, leadership_level: int):
        Person.__init__(self, name, surname, age, nationality)
        self.number = number
        self._position = position
        self.__average_points = average_points
        self.__experience = experience
        self._specialization = specialization
        self.leadership_level = leadership_level

    def lead_training_session(self):
        print(f"Playing Coach {self.name} is leading the training session. Combining training drills with tactical advice.")

    def analyze_performance(self):
        print(f"Playing Coach {self.name} is analyzing both their own and the team's performance.")

    def motivate_team(self):
        print(f"Playing Coach {self.name} is motivating the team before the match. Leadership level: {self.leadership_level}")

    def __str__(self):
        return f"{Person.__str__(self)}, Number: {self.number}, Position: {self._position}, Average Points: {self.__average_points}, Experience: {self.__experience}, Specialization: {self._specialization}, Leadership Level: {self.leadership_level}"
