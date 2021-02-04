class Calculator:
    def power(self, n, p):
        if n >= 0 and p >= 0:
            return n ** p
        else:
            raise Exception("n and p should be non-negative")


myCalculator = Calculator()
T = 2
nums = [2, 3]

for i in range(T):
    n, p = map(int, nums)

    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
