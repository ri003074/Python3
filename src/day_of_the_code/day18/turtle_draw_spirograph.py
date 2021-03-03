from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.circle(100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
