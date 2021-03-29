import random

names = ["Alex", "Beth", "John", "Jack", "Jun"]

students_score = {name: random.randint(1, 100) for name in names}
print(students_score)

passed_students = {key: value for key, value in students_score.items() if value > 50}
print(passed_students)