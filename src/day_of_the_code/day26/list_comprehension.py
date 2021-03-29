numbers = [
    1,
    2,
    3,
]

new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Kenta"
new_name = [letter for letter in name]
print(new_name)


new_numbers = [i * 2 for i in range(1, 5)]
print(new_numbers)

names = ["aaaaaaaaaaaa", "bbb", "cccccccc"]
new_names = [name.upper() for name in names if len(name) > 5]
print(new_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

new_numbers = [num for num in numbers if num % 2 == 0]
print(new_numbers)


f1_l = []
f2_l = []
with open("file1.txt") as f1:
    f1_l = f1.readlines()
with open("file2.txt") as f2:
    f2_l = f2.readlines()

print(f1_l)
print(f2_l)

dup_l = [int(num) for num in f1_l if num in f2_l]
print(dup_l)
