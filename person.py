class Person:
    def __init__(self, name: str, surname: str, age: int, nationality: str):
        self.name = name
        self._surname = surname
        self.age = age
        self.__nationality = nationality

    def get_info(self) -> str:
        return f"Name: {self.name}, Surname: {self._surname}, Age: {self.age}, Nationality: {self.__nationality}"

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    def __str__(self):
        return self.get_info()

    @property
    def nationality(self):
        return self.__nationality

    def set_nationality(self, nationality):
        if isinstance(nationality, str):
            self.__nationality = nationality
        else:
            raise ValueError('nationality must be a string')
