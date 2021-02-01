height = 1.63
weight = 48

bmi = round(48 / 1.63 ** 2)
print(bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
