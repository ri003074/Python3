import time


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"{number} is prime number")
    else:
        print(f"{number} is not prime number")


start = time.time()
for i in range(1, 100):
    prime_checker(i)

elapsed_time = time.time()

print(elapsed_time - start)
