class Staff:
    def __init__(self, role: str, experience: int):
        self.__role = role
        self.__experience = experience

    def get_role(self) -> str:
        return self.__role

    def get_experience(self) -> int:
        return self.__experience

    def get_staff_info(self):
        return f"Role: {self.__role}, Experience: {self.__experience} years"

    @staticmethod
    def valid_experience(experience: int) -> bool:
        return experience >= 0

    def __str__(self):
        return self.get_staff_info()
