n = 5
m = 3
data = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
k = 2

# order_key = [x[k] for x in data]
# order_key_data = [x, y for x, y in zip(order_key, data)]
# order_key_data_sorted = sorted(order_key_data.items())
# print(order_key)
# print(order_key_data)

# for val in order_key_data_sorted:
#     for i in range(m):
#         print(val[1][i], end=" ")
#     print("")

# arr1 = [1, 2, 3]
# arr2 = [[4], [5], [6]]

# arr_new = [[x for x in arr1] for y in arr2]

# arr = []
# for i, y in zip(arr1, arr2):
#     arr.append([i, y])

# print(arr)


# order_key = [x[k] for x in data]

# arr_new = []
# for i, j in zip(order_key, data):
#     arr_new.append([i, j])

# arr_new_sorted = sorted(arr_new)
# print(arr_new)
# print(arr_new_sorted)

# for i in arr_new_sorted:
#     for j in range(m):
#         print(i[1][j], end=" ")
#     print("")


data = sorted(data, key=lambda x: x[k])

for i in range(n):
    for j in range(m):
        print(data[i][j], end=" ")
    print("")
