from person import Person
from player import Player
from coach import Coach
from medical_staff import MedicalStaff
from staff import Staff

# Створення екземплярів кожного класу
person = Person("Alice", "Smith", 30, "USA")
player = Player("Bob", "Johnson", 25, "Canada", 23, "shooting guard", 15.5)
coach = Coach("Charlie", "Brown", 50, "UK", 25, "Defensive")
med_staff = MedicalStaff("Daisy", "Miller", 35, "Australia", "Physiotherapist", 10, "Sports Medicine")

# Виклик методів і робота з властивостями
print("=== Person ===")
print(person)
person.set_nationality("UK")
print(f"Updated Nationality: {person.nationality}")
print(f"Is Adult: {Person.is_adult(person.age)}")

print("\n=== Player ===")
print(player)
player.train()
player.play_match(20)
player.average_points = (player.average_points + 20) / 2
print(f"Updated Average Points: {player.average_points}")

print("\n=== Coach ===")
print(coach)
coach.give_instructions(player)
coach.plan_training()
coach.set_experience(30)
print(f"Updated Experience: {coach.experience}")

print("\n=== Medical Staff ===")
print(med_staff)
med_staff.treat_player(player._name)
med_staff.provide_medical_help()
med_staff.set_specialization("Orthopedic")
print(f"Updated Specialization: {med_staff.specialization}")

# Поліморфізм - виклик __str__() для різних класів
print("\n=== Поліморфізм ===")
people = [person, player, coach, med_staff]
for p in people:
    print(p)

# Використання базових методів роботи з предметною областю
print("\n=== Використання базових методів ===")
staff = Staff("Manager", 5)
print(staff)
if Staff.valid_experience(staff.get_experience()):
    print("The staff member has valid experience.")
else:
    print("The staff member has invalid experience.")
