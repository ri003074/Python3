from turtle import Turtle, Screen


screen = Screen()
turtle = Turtle()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="r", fun=turn_right)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
