s = "My name is Mike. Hi Mike"
print(s)

is_start = s.startswith("My")
print(is_start)

is_start = s.startswith("name")
print(is_start)


print(s.find("Mike"))
print(s.rfind("Mike"))
print(s.count("Mike"))
print("capitalize")
print(s.capitalize())
print("title")
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace("Mike", "Nancy"))


print("a is {} {}".format(1, 2))

print("a is {1} {0}".format(1, 2))

print("My name is {0} {1}. I am {1} {0}".format("Jun", "Sakai"))

print(
    "My name is {name} {family}. I am {family} {name}".format(
        name="Jun", family="Sakai"
    )
)


x = 1
print(type(x))

x = str(1)
print(type(x))


a = "a"
print(f"a is {a}")

x, y, z = 1, 2, 3
print(f"a is {x}, {y}, {z}")

name = "kenta"
family = "kawa"

print(f"My name is {name} {family}. I am {family} {name}")
