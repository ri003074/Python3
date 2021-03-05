input = input()
input_list = input.split(",")

output_list = []
for i in range(len(input_list)):
    if i % 2 or input_list[i - 1] == input_list[i]:
        output_list.append(input_list[i])

print(",".join(output_list))


"""
input = "1,2,3,4,4,6,7"
        print(input_list[i])
print(input_list)
"""
