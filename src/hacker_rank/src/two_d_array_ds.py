arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

result = []
for i in range(4):
    for j in range(4):
        sum = (
            arr[j][i]
            + arr[j][i + 1]
            + arr[j][i + 2]
            + arr[j + 1][i + 1]
            + arr[j + 2][i]
            + arr[j + 2][i + 1]
            + arr[j + 2][i + 2]
        )
        result.append(sum)


print(max(result))
