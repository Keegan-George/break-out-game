from turtle import Turtle
from config import BrickConfig


class Brick(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape(BrickConfig.SHAPE)
        self.shapesize(stretch_len=BrickConfig.STRETCH_LENGTH)
        self.point: int | None = None
        self.penup()

    def remove(self) -> None:
        """
        Remove brick by hiding it and moving it to an off screen location.
        """
        self.goto(BrickConfig.OFF_SCREEN_LOCATION)
        self.hideturtle()
        self.clear()
