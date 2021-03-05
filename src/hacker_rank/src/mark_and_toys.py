def maximumToys(prices, k):
    prices = sorted(prices)
    print(prices)

    total = 0
    for i in range(len(prices)):
        total += prices[i]

        if total > k:
            break
    return i


print(maximumToys([1, 12, 5, 111, 2000, 1000, 10], 50))
