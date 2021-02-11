def greeting():
    yield "Good Morning"
    yield "Good afternoon"
    yield "Good night"


g = greeting()

print(next(g))
print("@@@@@@@@@@@@@@")
print(next(g))
print("@@@@@@@@@@@@@@")
print(next(g))


def gen():
    for i in range(10):
        yield i


gen = gen()
print(type(gen))

gene2 = (i for i in range(10))
print(type(gene2))
print(next(gene2))
print(next(gene2))
print(next(gene2))

gene3 = (i for i in range(10) if i % 2 == 0)

for x in gene3:
    print(x)
