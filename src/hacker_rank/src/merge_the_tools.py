# def merge_the_tools(string, k):
#     str_list = []
#     for index in range(0, len(string), k):
#         str_list.append((string[index : index + k]))

#     for str_var in str_list:
#         tmp = []
#         tmp.append(str_var[0])
#         for i in range(0, len(str_var)):
#             if str_var[0] != str_var[i] and str_var[i] not in tmp:
#                 tmp.append(str_var[i])

#         print("".join(tmp))


def merge_the_tools(string, k):
    num_subsegments = int(len(string) / k)
    for i in range(0, num_subsegments):
        t = string[i * k : (i + 1) * k]

        u = ""
        for c in t:
            if c not in u:
                u += c

        print(u)


merge_the_tools("AABCAAADA", 3)
merge_the_tools("AAABCADDE", 3)


"""
s = input()
k = int(input())
num_subsegments = int(len(s) / k)

for index in range(num_subsegments):
    # Subsegment string
    t = s[index * k : (index + 1) * k]

    # Subsequence string having distinct characters
    u = ""

    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
            u += c

    # Print final converted string
    print(u)
"""
