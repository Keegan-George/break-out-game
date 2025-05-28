from config import BallConfig, ScreenConfig, DEFAULT_TURTLE_SIZE
from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape(BallConfig.SHAPE)
        self.color(BallConfig.COLOUR)
        self.penup()
        self.goto(BallConfig.starting_position())
        self.x_move = BallConfig.MOVE_DISTANCE
        self.y_move = BallConfig.MOVE_DISTANCE

    def move(self) -> None:
        """ "
        Move the ball.
        """
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self) -> None:
        """
        Reverse the direction of the ball along itx x-trajectory.
        """
        self.x_move *= -1

    def bounce_y(self) -> None:
        """
        Reverse the direction of the ball along its y-trajectory.
        """
        self.y_move *= -1

    def has_hit_upper_wall(self):
        """
        Return True if the ball has hit the upper wall. False otherwise.

        """
        return self.ycor() + BallConfig.BALL_RADIUS >= ScreenConfig.HEIGHT // 2

    def has_hit_side_wall(self) -> bool:
        """
        Return True if the ball has hit either of the side walls. False otherwise.
        """
        return (
            self.xcor() + BallConfig.BALL_RADIUS >= ScreenConfig.WIDTH // 2
            or self.xcor() - BallConfig.BALL_RADIUS <= -ScreenConfig.WIDTH // 2
        )

    def has_hit_other_object(self, object: Turtle):
        """
        Return True if the ball has collided with another object; paddle or brick. False otherwise.
        """
        object_height = object.shapesize()[0] * DEFAULT_TURTLE_SIZE  # stretch_wid
        object_width = object.shapesize()[1] * DEFAULT_TURTLE_SIZE  # stretch_len

        return (
            self.xcor() - BallConfig.BALL_RADIUS < object.xcor() + object_width / 2
            and self.xcor() + BallConfig.BALL_RADIUS > object.xcor() - object_width / 2
            and self.ycor() - BallConfig.BALL_RADIUS < object.ycor() + object_height / 2
            and self.ycor() + BallConfig.BALL_RADIUS > object.ycor() - object_height / 2
        )

    def is_below_screen(self):
        """
        Return True if the ball has gone below the screen. False otherwise.
        """
        return self.ycor() < -ScreenConfig.HEIGHT // 2
