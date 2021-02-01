if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    for i in range(n):
        print(arr[n - i - 1], end="")


print(" ".join(map(str, reversed(arr))))
