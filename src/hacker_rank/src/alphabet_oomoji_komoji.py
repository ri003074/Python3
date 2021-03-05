input = input()
input_list = input.split(" ")

phrase_list = []
for i in range(len(input_list)):
    if input_list[i][0].istitle() is True or input_list[i][0].isdecimal() is True:
        phrase_list.append(input_list[i])


phrase_list_rm_duplicate = set(phrase_list)
print(len(phrase_list_rm_duplicate))


#        print(phrase[i][0])
# print(phrase)
# input = "Ab bc cd De 1"
