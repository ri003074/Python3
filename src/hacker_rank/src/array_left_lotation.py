def rotLeft(a, d):
    arr_s_r = a.split(" ")
    arr_d = d.split(" ")
    print(arr_s_r)

    return arr_d[int(arr_s_r[1]) :] + arr_d[: int(arr_s_r[1])]


result = rotLeft("5 4", "1 2 3 4 5")
print(" ".join(map(str, result)))
