import time

start = time.time()
n = 4
arr = [57, 57, 57, -57]
# arr = [2, 3, 6, 6, 5]

# arr_sorted = sorted(arr, reverse=True)
# print(arr_sorted)

# for i in range(1, n):
#     if arr_sorted[i] != arr_sorted[i - 1]:
#         print(arr_sorted[i])
#         break

# setを使えば、-2で出来たな


arr_new = list(set(arr))
arr_new.sort()
print(arr_new)
print(arr_new[-2])


print(f" elapsed time = {time.time() - start} sec")
