class Fish:
    def __init__(self, name, build="hone", eyelids=False):
        self.name = name
        self.build = build
        self.eyelids = eyelids

    def swim(self):
        print("can swim")

    def swim_back(self):
        print("can swim back")


class Medaka(Fish):
    pass


medaka = Medaka("medaka")
medaka.swim()


class Cat:
    def __init__(self, name):
        self.name = name


class SuperCat(Cat):
    def __init__(self, name, function):
        super(SuperCat, self).__init__(name)
        self.function = function


sample1 = Cat("cat1")
sample2 = SuperCat("cat2", "fly")

print(sample1.name)
print(sample2.name, sample2.function)