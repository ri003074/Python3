import time


def prime_checker(number):
    counter = 0
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            counter += 1

    if counter == 2:
        print(f"{number} is prime number")
    else:
        print(f"{number} is not prime number")


start = time.time()
for i in range(1, 10000):
    prime_checker(i)

elapsed_time = time.time()

print(elapsed_time - start)
