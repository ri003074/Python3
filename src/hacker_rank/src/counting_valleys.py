# def countingValleys(steps, path):
#     path_to_num = []
#     valley_count = 0
#     path_to_num_counter = 0
#     path_list = list(path)

#     for i in path_list:
#         if i == "U":
#             path_to_num_counter += 1
#         else:
#             path_to_num_counter -= 1

#         path_to_num.append(path_to_num_counter)

#     print(path_to_num)
#     if path_to_num[0] == -1:
#         valley_count += 1
#     for j in range(len(path_to_num) - 1):
#         if path_to_num[j] == 0 and path_to_num[j + 1] < 0:
#             valley_count += 1

#     return valley_count


# print(countingValleys(8, "UDDDUDUU"))
# print(countingValleys(12, "DDUUDDUDUUUD"))


"""
8 stepだと、4U, 4D
"""


height = 0
prev_height = 0
cnt = 0

s = "UDDDUDUU"
# s = "DDUUDDUDUUUD"

for i in range(len(s)):
    if s[i] == "U":
        height += 1
    elif s[i] == "D":
        height -= 1
    if height == 0 and prev_height < 0:
        cnt += 1
    prev_height = height

print(cnt)
