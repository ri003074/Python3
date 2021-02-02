size = "L"
add_pepperoni = "Y"
extra_cheese = "N"

bill = 0

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2

# if size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
# if size == "L":
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(bill)
