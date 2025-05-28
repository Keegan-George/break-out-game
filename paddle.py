from config import *
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOUR)
        self.shapesize(stretch_len=PADDLE_STRETCH_LENGTH)
        self.penup()
        self.goto(PADDLE_STARTING_X_POSITION, PADDLE_Y_POSITION)

    def move_left(self):
        self.goto(self.xcor() - PADDLE_MOVE_DISTANCE, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + PADDLE_MOVE_DISTANCE, self.ycor())
