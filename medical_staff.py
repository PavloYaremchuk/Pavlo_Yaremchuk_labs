from person import Person
from staff import Staff

class MedicalStaff(Person, Staff):
    def __init__(self, name: str, surname: str, age: int, nationality: str, role: str, experience: int, specialization: str):
        Person.__init__(self, name, surname, age, nationality)
        Staff.__init__(self, role, experience)
        self.__specialization = specialization

    def get_specialization(self) -> str:
        return self.__specialization

    def get_medical_staff_info(self) -> str:
        return f"Specialization: {self.__specialization}"

    def treat_player(self, player_name: str):
        print(f"{self._name} is treating {player_name} with specialization in {self.__specialization}.")

    def __str__(self):
        return f"{Person.__str__(self)}, {Staff.__str__(self)}, {self.get_medical_staff_info()}"

    @property
    def specialization(self):
        return self.__specialization

    def set_specialization(self, specialization):
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            raise ValueError('Specialization must be a string')

    def display_message(func):
        def wrapper(*args, **kwargs):
            print("Medical staff is about to perform an action.")
            return func(*args, **kwargs)
        return wrapper

    @display_message
    def provide_medical_help(self):
        print(f"{self._name} is providing medical help.")
