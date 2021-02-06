n = 3
a = [4, 3, 1, 2]

swapped = 0
for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped += 1

print(f"Array is sorted in {swapped} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
