from turtle import Turtle, Screen

turtle = Turtle()


for i in range(3, 10):
    deg = 360 / i
    num = 360 / deg
    for _ in range(int(num)):
        turtle.forward(100)
        turtle.right(deg)

screen = Screen()
screen.exitonclick()
