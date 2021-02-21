file = "./input.txt"
arr = []
with open(file, "r") as f:
    for line in f.read().splitlines():
        print(line)
        arr.append(line)


print(arr)