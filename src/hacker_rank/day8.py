if __name__ == "__main__":
    dic = {}
    n = int(input())
    for i in range(n):
        arr = list(input().rstrip().split())
        dic[arr[0]] = arr[1]

    while True:
        try:
            name = input()
            if name in dic:
                print(f"{name}={dic[name]}")
            else:
                print("Not found")
        except EOFError:
            break


# n = int(input())
# name_numbers = [input().split() for _ in range(n)]
# phone_book = {k: v for k, v in name_numbers}
# while True:
#     try:
#         name = input()
#         if name in phone_book:
#             print("%s=%s" % (name, phone_book[name]))
#         else:
#             print("Not found")
#     except EOFError:
#         break
