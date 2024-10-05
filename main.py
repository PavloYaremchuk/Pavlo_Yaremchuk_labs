from person import Person
from player import Player
from coach import Coach
from medical_staff import MedicalStaff
from playing_coach import PlayingCoach

# Створення екземплярів кожного класу
person = Person("Alice", "Smith", 30, "USA")
player = Player("Bob", "Johnson", 25, "Canada", 23, "shooting guard", 15.5)
coach = Coach("Charlie", "Brown", 50, "UK", 25, "Defensive")
med_staff = MedicalStaff("Daisy", "Miller", 35, "Australia", "Physiotherapist", 10, "Sports Medicine")
playing_coach = PlayingCoach("Eve", "Adams", 40, "Germany", 9, "point guard", 12.5, 15, "Offensive", 8)

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
med_staff.treat_player(player.name)
med_staff.provide_medical_help()
med_staff.set_specialization("Orthopedic")
print(f"Updated Specialization: {med_staff.specialization}")

print("\n=== Playing Coach ===")
print(playing_coach)
playing_coach.train()
playing_coach.give_instructions(player)
playing_coach.lead_training_session()
playing_coach.analyze_performance()
playing_coach.motivate_team()

# Поліморфізм - виклик __str__() для різних класів
print("\n=== Поліморфізм ===")
people = [person, player, coach, med_staff, playing_coach]
for p in people:
    print(p)
