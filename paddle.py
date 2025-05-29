from turtle import Turtle
from config import PaddleConfig, ScreenConfig


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape(PaddleConfig.SHAPE)
        self.color(PaddleConfig.COLOUR)
        self.shapesize(stretch_len=PaddleConfig.STRETCH_LENGTH)
        self.penup()
        self.goto(PaddleConfig.starting_position())

    def move(self, direction: str):
        """
        Move the paddle left or right accordingly based on the direction passed.
        Prevents the paddle from going out of bounds.
        """
        direction_map = {
            "left": -PaddleConfig.MOVE_OFFSET,
            "right": PaddleConfig.MOVE_OFFSET,
        }

        if direction not in direction_map:
            raise ValueError("Direction must be 'left' or 'right'.")

        half_paddle_width = PaddleConfig.paddle_length() // 2
        left_boundary = -ScreenConfig.WIDTH // 2 + half_paddle_width
        right_boundary = ScreenConfig.WIDTH // 2 - half_paddle_width

        xcoor = self.xcor() + direction_map[direction]

        if left_boundary < xcoor < right_boundary:
            self.goto(xcoor, self.ycor())
