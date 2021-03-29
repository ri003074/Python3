names = ["Alan", "John", "Job"]

for i in range(len(names)):
    print(names[i])

for idx, value in enumerate(names):
    print(idx, value)

for idx, value in enumerate(names, start=1):
    print(idx, value)


nik = {
    "age": 32,
    "gender": "male",
    "employed": True,
}

# print(nik["location"])

print(nik.get("location"))

names = ["Nik", "Jane", "Melissa", "Doug"]
ages = [32, 28, 37, 53]
gender = ["Male", "Female", "Female", "Male"]

# Old boring way:
for_looped = []
for i in range(len(names)):
    for_looped.append((names[i], ages[i], gender[i]))

print(for_looped)

# Zipping through lists with zip()
zipped = zip(names, ages, gender)
zipped_list = list(zipped)

print(zipped_list)

ages = dict(zip(names, ages))

print(ages)


some_variable = "HELLO!"

print(f"some_variable={some_variable}")
print(f"{some_variable=}")
