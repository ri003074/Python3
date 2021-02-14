import math


def calc_cans(test_h, test_w):
    coverage = 5

    number_of_cans = math.ceil((test_h * test_w) / coverage)

    return number_of_cans


print(calc_cans(2, 4))
print(calc_cans(3, 9))
