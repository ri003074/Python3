from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]

all_turtles = []
is_rance_on = False

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

is_rance_on = True

while is_rance_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_rance_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print("You win!")
            else:
                print(f"You loose. winning color is {winning_color}")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
