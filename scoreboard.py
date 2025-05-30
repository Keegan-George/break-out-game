from turtle import Turtle
from config import ScoreBoardConfig


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color(ScoreBoardConfig.COLOUR)
        self.lives: int = ScoreBoardConfig.LIVES
        self.score: int = 0
        self.hideturtle()
        self.penup()
        self.goto(ScoreBoardConfig.location())
        self.refresh_scoreboard()

    def refresh_scoreboard(self) -> None:
        """
        Clear and refresh the scoreboard.
        """
        self.clear()
        self.display_score()

    def display_score(self) -> None:
        """
        Display the current score and the number of lives remaining.
        """
        self.write(
            f"Score: {self.score}   Lives: {self.lives}",
            align="center",
            font=ScoreBoardConfig.FONT,
        )

    def display_message(self, result: str) -> None:
        """
        Display a message in the center of the screen.
        """
        self.goto(0, 0)
        self.write(result, align="center", font=ScoreBoardConfig.FONT)
