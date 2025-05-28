from config import *
from turtle import Turtle


class Brick(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=BRICK_STRETCH_LENGTH)
        self.penup()

    def remove(self):
        self.reset()

        # since turtle objects cannot be deleted move it off screen
        self.goto(10000, 10000)
