num = 6

sum = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        sum += i

print(sum)


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for i in range(1, n + 1):
            if num % i == 0:
                print(i)
                sum += i

        return sum


n = 6
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
