row1 = ["M", "M", "M"]
row2 = ["M", "M", "M"]
row3 = ["M", "M", "M"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

input_num = list("23")

print(input_num)
map[int(input_num[0]) - 1][int(input_num[1]) - 1] = "X"
print(map)
