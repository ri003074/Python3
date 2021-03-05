import matplotlib.pyplot as plt
import numpy as np
import hello

x = np.arange(0, 100, 0.5)
Hz = 5.0
y = np.sin(2.0 * np.pi * (x * Hz) / 100)

plt.plot(x, y)
plt.savefig("sample.png")


hello.konchiwa("taro")

list = [1, 2, 3, 4]


def hello():
    print("hello")
    print("hehe")


def foo():
    print("Hello" "World")

enumerate