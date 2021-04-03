import random

names = ["Alex", "Beth", "John", "Jack", "Jun"]

students_score = {name: random.randint(1, 100) for name in names}
print(students_score)

passed_students = {key: value for key, value in students_score.items() if value > 50}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split(" ")
print(sentence_list)
new_sentence_dict = {sentence: len(sentence) for sentence in sentence.split()}
print(new_sentence_dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# (temp_c * 9/5) + 32 = temp_f

weather_f = {day: temp * 9 / 5 + 32 for day, temp in weather_c.items()}
print(weather_f)
