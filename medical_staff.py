from person import Person

class MedicalStaff(Person):
    def __init__(self, name: str, surname: str, age: int, nationality: str, role: str, experience: int, specialization: str):
        super().__init__(name, surname, age, nationality)
        self.__role = role
        self.__experience = experience
        self.__specialization = specialization

    def get_specialization(self) -> str:
        return self.__specialization

    def get_medical_staff_info(self) -> str:
        return f"Role: {self.__role}, Experience: {self.__experience} years, Specialization: {self.__specialization}"

    def treat_player(self, player_name: str):
        print(f"{self.name} is treating {player_name} with specialization in {self.__specialization}.")

    def __str__(self):
        return f"{super().__str__()}, {self.get_medical_staff_info()}"

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
        print(f"{self.name} is providing medical help.")
