from turtle import Screen
from puddle import Puddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Arcade Game")
screen.bgcolor("black")
screen.tracer(0)  # turn off the animation

r_puddle = Puddle((350, 0))
l_puddle = Puddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_puddle.up)
screen.onkey(key="Down", fun=r_puddle.down)
screen.onkey(key="w", fun=l_puddle.up)
screen.onkey(key="s", fun=l_puddle.down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (
        ball.distance(r_puddle) < 80
        and ball.xcor() > 320
        or ball.distance(l_puddle) < 80
        and ball.xcor() < -320
    ):
        print("contact")
        ball.bounce_x()

    elif ball.xcor() > 340:
        ball.reset()
        ball.bounce_x()
        scoreboard.increase_l_score()
        scoreboard.update_score()

    elif ball.xcor() < -340:
        ball.reset()
        ball.bounce_x()
        scoreboard.increase_r_score()
        scoreboard.update_score()

screen.exitonclick()
