y = [1, 2, 3]
x = 1

if x in y:
    print("in")


if 1000 not in y:
    print("not in")


is_ok = True
if not is_ok:
    print("hello")


if is_ok:
    print("ok")


# 中身が入っているかどうかをチェックできる
is_ok = []

if is_ok:
    print("ok")
else:
    print("no")


is_empty = None
print(is_empty)

# is is for None object
# None を判定するときによく使われる
if is_empty is None:
    print("None!!")


# print(1 == True)
# print(1 is True)
