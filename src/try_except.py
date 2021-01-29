lst = [1, 2, 3]
i = 5

try:
    lst[i]
except IndexError as ex:
    print("dont worry: {}".format(ex))
finally:
    print("clean up")


print("last")


# raise IndexError("test error")


class UppercaseError(Exception):
    pass


def check():
    words = ["APPLE", "orange", "banana"]
    for word in words:
        raise UppercaseError(word)


try:
    check()
except UppercaseError as exc:
    print(f"this is my fault {exc}")
