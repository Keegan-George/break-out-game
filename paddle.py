from turtle import Turtle
from config import PaddleConfig


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape(PaddleConfig.SHAPE)
        self.color(PaddleConfig.COLOUR)
        self.shapesize(stretch_len=PaddleConfig.STRETCH_LENGTH)
        self.penup()
        self.goto(PaddleConfig.starting_position())

    def move_left(self):
        """
        Moves the paddle to the left.
        """
        self.goto(self.xcor() - PaddleConfig.MOVE_DISTANCE, self.ycor())

    def move_right(self):
        """
        Moves the paddle to the right. 
        """
        self.goto(self.xcor() + PaddleConfig.MOVE_DISTANCE, self.ycor())
