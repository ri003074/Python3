from time import perf_counter

if __name__ == '__main__':
    start = perf_counter()

    for i in range(100000):
        print(i)

    end = perf_counter()

    print(end - start)
