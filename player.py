from person import Person

class Player(Person):
    def __init__(self, name, surname, age: int, nationality: str, number: int, position: str, average_points: float):
        super().__init__(name, surname, age, nationality)
        self.number = number
        self._position = position
        self.__average_points = average_points

    def train(self):
        print(f"Player {self._name} is training.")

    def play_match(self, points_scored: int):
        self.average_points = (self.average_points + points_scored) / 2
        print(f"Player {self._name} scored {points_scored} points in the match.")

    def get_player_info(self):
        return f"Number: {self.number}, Position: {self._position}, Average Points: {self.__average_points}"

    @staticmethod
    def player_position_valid(position: str) -> bool:
        valid_positions = ["point guard", "shooting guard", "small forward", "power forward", "center"]
        return position in valid_positions

    def __str__(self):
        return f"{super().__str__()}, {self.get_player_info()}"

    @property
    def average_points(self):
        return self.__average_points

    @average_points.setter
    def average_points(self, points):
        if points >= 0:
            self.__average_points = points
        else:
            raise ValueError('Average points must be a non-negative number')
