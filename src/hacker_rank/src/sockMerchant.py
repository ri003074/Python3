def sockMerchant(n, ar):
    ar_set = set(ar)
    result = 0

    for i in ar_set:
        print(ar.count(i) // 2)
        result += ar.count(i) // 2

    return result


arr = [1, 2, 2, 3, 1, 1]
num = 5

print(sockMerchant(num, arr))
