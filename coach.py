from person import Person
from player import Player

class Coach(Person):
    def __init__(self, name: str, surname: str, age: int, nationality: str, experience: int, specialization: str):
        super().__init__(name, surname, age, nationality)
        self.__experience = experience
        self._specialization = specialization

    def give_instructions(self, player: Player):
        print(f"Coach {self._name} is giving instructions to {player._name}.")

    def plan_training(self):
        print(f"Coach {self._name} is planning a training session.")

    def get_coach_info(self):
        return f"Experience: {self.__experience}, Specialization: {self._specialization}"

    @staticmethod
    def valid_experience(experience: int) -> bool:
        return experience >= 0

    def __str__(self):
        return f"{super().__str__()}, {self.get_coach_info()}"

    @property
    def experience(self):
        return self.__experience

    def set_experience(self, years):
        if years >= 0:
            self.__experience = years
        else:
            raise ValueError('Experience must be non_negative number')
