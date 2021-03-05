#!/bin/python3

# Complete the minimumSwaps function below.
# def minimumSwaps(arr):
#     swap = 0
#     for i in range(len(arr)):
#         if arr[i] != i + 1:
#             index = arr.index(i + 1)
#             arr[i], arr[index] = arr[index], arr[i]
#             swap += 1
#             # for j in range(i, len(arr)):
#             #     if i + 1 == arr[j]:
#             #         tmp = arr[i]
#             #         arr[i] = i + 1
#             #         arr[j] = tmp
#             #         swap += 1
#     return swap

"""
listを検索するよりも、dictionaryを検索する方が早い
"""


def minimumSwaps(arr):
    swap = 0
    ref_arr = sorted(arr)
    index_dic = {v: i for i, v in enumerate(arr)}

    for index, value in enumerate(arr):
        correct_value = ref_arr[index]
        if value != correct_value:
            to_swap_ix = index_dic[correct_value]
            arr[to_swap_ix], arr[index] = arr[index], arr[to_swap_ix]
            index_dic[value] = to_swap_ix
            index_dic[correct_value] = index
            swap += 1

    return swap


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # n = int(input())

    # arr = list(map(int, input().rstrip().split()))

    arr = [4, 3, 1, 2]
    # arr = [7, 1, 3, 2, 4, 5, 6]
    res = minimumSwaps(arr)
    print(res)

    # fptr.write(str(res) + "\n")

    # fptr.close()
