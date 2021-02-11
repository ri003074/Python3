"""
show difference between is and ==

"==" compare the value
"is" compare the address

"is" is faster
"""

import time


var1 = 1
var2 = 1
print(hex(id(var1)))
print(hex(id(var2)))
print(var1 == var2)
print(var1 is var2)


def compare(n):
    # var1 = 1
    # var2 = 1
    var1 = "abc"
    var2 = "abc"

    for _ in range(n):
        if var1 == var2:
            # if var1 is var2:
            pass


start = time.perf_counter()
compare(100000000)
end = time.perf_counter()

print("total = ", end - start)
