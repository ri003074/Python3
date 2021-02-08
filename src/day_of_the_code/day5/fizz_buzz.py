for num in range(101):

    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
    else:
        print(num)
