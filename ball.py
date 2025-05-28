from config import *
from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOUR)
        self.penup()
        self.goto(BALL_STARTING_X_POSITION, BALL_STARTING_Y_POSITION)
        self.x_move = BALL_MOVE_DISTANCE
        self.y_move = BALL_MOVE_DISTANCE

    def move(self) -> None:
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self) -> None:
        self.x_move *= -1

    def bounce_y(self) -> None:
        self.y_move *= -1

    def has_collided_with_upper_wall(self):
        return self.ycor() + BALL_RADIUS >= SCREEN_HEIGHT // 2

    def has_collided_with_side_wall(self):
        return (
            self.xcor() + BALL_RADIUS >= SCREEN_WIDTH // 2
            or self.xcor() - BALL_RADIUS <= -SCREEN_WIDTH // 2
        )

    def has_collided_with_other_object(self, object: Turtle):
        object_width = object.shapesize()[0] * BASE_TURTLE_LENGTH
        object_length = object.shapesize()[1] * BASE_TURTLE_LENGTH

        return (
            self.xcor() - BALL_RADIUS < object.xcor() + object_length / 2
            and self.xcor() + BALL_RADIUS > object.xcor() - object_length / 2
            and self.ycor() - BALL_RADIUS < object.ycor() + object_width / 2
            and self.ycor() + BALL_RADIUS > object.ycor() - object_width / 2
        )

    def has_gone_below_screen(self):
        return self.ycor() < -SCREEN_HEIGHT // 2
