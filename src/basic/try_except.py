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


try:
    file = open("a.txt")
    dic = {"key": "value"}
    # key = dic["sfds"]

except FileNotFoundError:
    file = open("a.txt", "w")
    file.write("something")

except KeyError as error:
    print(f"{error} doesn't exsist")

else:
    content = file.read()
    print(content)

finally:
    file.close()


height = 40
widht = 30

if height > 3:
    raise ValueError("human height should not be over 3 meters")
