def countSwap(a):
    counter = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                counter += 1

    print(f"Array is sorted in {counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


countSwap([3, 2, 1])
