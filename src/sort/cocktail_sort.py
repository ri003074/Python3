from typing import List


def coktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        start = start + 1

    return numbers


if __name__ == "__main__":
    nums = [1, 3, 4, 5, 8, 7]
    print(coktail_sort(nums))
