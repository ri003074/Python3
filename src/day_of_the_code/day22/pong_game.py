from turtle import Screen
from puddle import Puddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Arcade Game")
screen.bgcolor("black")
screen.tracer(0)  # turn off the animation

r_puddle = Puddle((350, 0))
l_puddle = Puddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=r_puddle.up)
screen.onkey(key="Down", fun=r_puddle.down)
screen.onkey(key="w", fun=l_puddle.up)
screen.onkey(key="s", fun=l_puddle.down)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

screen.exitonclick()
