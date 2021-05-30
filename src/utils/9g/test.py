import sys

abc = ["abc", "def", "ghi"]

dic = {"abc": "AAA", "def": "DDD"}


for i in range(len(abc)):
    for key, value in dic.items():
        if abc[i] == key:
            abc[i] = value

print(abc)


class Outer:
    def __init__(self):
        print("create Outer Class")
        print(self.Inner)
        # self.Innerのメモリサイズを確認
        print(sys.getsizeof(self.Inner))
        self.inner = self.Inner()
        print(self.inner)

    class Inner:
        def __init__(self):
            print("create Inner Class")

        def abc(self):
            print("inner abc")


outer = Outer()

outer.inner.abc()
