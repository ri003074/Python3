import time

# print(arr)
# dic = defaultdict(int)

# if __name__ == "__main__":
#     start = time.time()
#     for i in range(1000):
#         for j in range(1000):
#             print(arr[i][j])
#     elapsed_time = time.time() - start
#     print("elapsed_time:{0}".format(elapsed_time) + "[sec]")


start = time.time()
arr = [[i * j for j in range(1000)] for i in range(1000)]
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

start = time.time()
dic = {str(i) + str(j): i * j for i in range(1000) for j in range(1000)}
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
