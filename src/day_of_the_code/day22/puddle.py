from turtle import Turtle

UP = 40
DOWN = 40


class Puddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + UP)

    def down(self):
        self.goto(self.xcor(), self.ycor() - DOWN)
