def prime_checker(number):
    print(number, end=":")
    if number == 1 or number == 2:
        print("prime number")

    if number >= 3:
        if number % 2 == 0:
            print("not prime number")
        else:
            print("prime number")


prime_checker(10)
for i in range(1, 100):
    prime_checker(i)
