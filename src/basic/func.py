val = [0]


def setVal(a):
    a.append(1)


setVal(val)
print(val)

# mutable変更可能な型だと、値の変更が保持される
# list, bytearray, set, dictionary

# immutable変更不可な型だと、値は保持されない
# int, float, complex, string, tuple, bytes, Frozen Set
#