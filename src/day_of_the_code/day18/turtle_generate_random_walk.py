from turtle import Turtle, Screen
from enum import IntEnum
import random

turtle = Turtle()
screen = Screen()
screen.colormode(255)


class Status(IntEnum):
    FORWARD = 1
    BACKWARD = 2
    RIGHT = 3
    LEFT = 4


def move_backward():
    turtle.color("green")
    turtle.backward(10)


def move_forward():
    turtle.color("red")
    turtle.forward(10)


def move_right():
    turtle.color("blue")
    turtle.right(90)
    turtle.forward(10)


def move_left():
    turtle.color("yellow")
    turtle.left(90)
    turtle.forward(10)


handlers = {
    Status.FORWARD.value: move_forward,
    Status.BACKWARD.value: move_backward,
    Status.RIGHT.value: move_right,
    Status.LEFT.value: move_left,
}


def handle_status_change(status):
    if status not in handlers:
        raise Exception(f"No handler found fot status: {status}")
    handler = handlers[status]
    handler()


choices = [
    Status.BACKWARD.value,
    Status.FORWARD.value,
    Status.RIGHT.value,
    Status.LEFT.value,
]

# for _ in range(100):
#     handle_status_change(random.choice(choices))

colors = ["red", "blue", "yellow", "green"]
directions = [0, 90, 180, 270]
turtle.pensize(15)
turtle.speed("fastest")
turtle.colormode = 255


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(100):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))


screen.exitonclick()
