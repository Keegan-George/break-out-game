from turtle import Turtle
from config import BrickConfig


class Brick(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape(BrickConfig.SHAPE)
        self.shapesize(stretch_len=BrickConfig.STRETCH_LENGTH)
        self.point = None
        self.penup()

    def remove(self):
        self.clear()
        self.hideturtle()
        self.goto(10000, 10000)
