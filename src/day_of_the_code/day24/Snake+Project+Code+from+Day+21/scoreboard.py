from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.read_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Score: {self.score} HighScore: {self.highscore}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset_scoreboard(self):
        self.clear()
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.highscore))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def read_highscore(self):
        with open("data.txt") as f:
            highscore = f.read()
            self.highscore = int(highscore)
