from turtle import Turtle
from config import ScoreBoardConfig


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color(ScoreBoardConfig.COLOUR)
        self.lives = ScoreBoardConfig.LIVES
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(ScoreBoardConfig.location())
        self.update_score()

    def update_score(self):
        """
        Updates the scoreboard with the latest score.
        """
        self.clear()
        self.write(
            f"Score: {self.score}   Lives: {self.lives}",
            align="center",
            font=ScoreBoardConfig.FONT,
        )

    def gameover(self):
        """
        Displays game over if the users loses all three lives.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=ScoreBoardConfig.FONT)

    def winner(self):
        """
        Displays winner if the user eliminates all bricks.
        """
        self.goto(0, 0)
        self.write("YOU WIN", align="center", font=ScoreBoardConfig.FONT)
