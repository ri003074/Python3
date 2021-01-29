class MyClass:
    def method(self):
        print("hello world")


x = MyClass()
x.method()


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def output(self):
        print("Point(%d, %d)" % (self._x, self._y))


p1 = Point(1, 2)
p2 = Point(3, 4)

p1.output()
p2.output()


class Point2(Point):
    print("Point2")


p3 = Point2(1, 2)
p3.output()


class GetData:
    def method(self):
        print("Get Data")

        return 1


x = GetData()
val = x.method()

print(val)


# class Person:
class Person(object):
    def __init__(self, name):
        self.name = name
        print("First")
        print(self.name)

    def say_something(self):
        print("I am {}, hello".format(self.name))

    def __del__(self):
        print("good bye")


kenta = Person("Mike")
kenta.say_something()


class Car(object):
    def run(self):
        print("run")


class ToyotaCar(Car):
    pass


car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()
