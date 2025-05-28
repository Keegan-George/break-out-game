from config import *
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.lives = LIVES
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(SCORE_X_POSITION, SCORE_Y_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}   Lives: {self.lives}", align="center", font=FONT
        )

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def winner(self):
        self.goto(0, 0)
        self.write("YOU WIN", align="center", font=FONT)
