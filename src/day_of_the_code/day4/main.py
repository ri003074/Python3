import my_module
import random

print(my_module.pi)
print(random.randint(1, 10))
print(random.random())
print(random.random() * 5 + 1)
print(random.random() * 9)


"""
Head and Tail
"""

random_num = random.randint(0, 1)

if random_num == 0:
    print("Heads")
else:
    print("Tails")
