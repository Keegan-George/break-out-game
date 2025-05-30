from turtle import Turtle
from brick import Brick
from paddle import Paddle
from config import BallConfig, ScreenConfig


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape(BallConfig.SHAPE)
        self.color(BallConfig.COLOUR)
        self.penup()
        self.radius = BallConfig.BALL_RADIUS
        self.x_move: float = None
        self.y_move: float = None
        self.reset()

    def move(self) -> None:
        """
        Move the ball.
        """
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self) -> None:
        """
        Reverse the ball x-trajectory.
        """
        self.x_move *= -BallConfig.SPEED_FACTOR

    def bounce_x_paddle(self, paddle: Paddle):
        """
        Reverse the ball x-trajectory based on where it made contact with the paddle.
        """
        x_dist = self.xcor() - paddle.xcor()
        self.x_move = x_dist * BallConfig.PADDLE_BOUNCE_FACTOR

    def bounce_y(self) -> None:
        """
        Reverse the ball y-trajectory.
        """
        self.y_move *= -BallConfig.SPEED_FACTOR

    def has_hit_upper_wall(self) -> bool:
        """
        Return True if the ball has hit the upper wall. False otherwise.
        """
        return self.ycor() + self.radius >= ScreenConfig.HEIGHT // 2

    def has_hit_side_wall(self) -> bool:
        """
        Return True if the ball has hit either of the side walls. False otherwise.
        """
        return (
            self.xcor() + self.radius >= ScreenConfig.WIDTH // 2
            or self.xcor() - self.radius <= -ScreenConfig.WIDTH // 2
        )

    def has_hit_other_object(self, object: Paddle | Brick) -> bool:
        """
        Return True if the ball has collided with a brick or the paddle. False otherwise.
        """
        return (
            self.xcor() - self.radius < object.xcor() + object.length / 2
            and self.xcor() + self.radius > object.xcor() - object.length / 2
            and self.ycor() - self.radius < object.ycor() + object.width / 2
            and self.ycor() + self.radius > object.ycor() - object.width / 2
        )

    def is_below_screen(self) -> bool:
        """
        Return True if the ball has gone below the screen. False otherwise.
        """
        return self.ycor() < -ScreenConfig.HEIGHT // 2

    def reset(self) -> None:
        """
        Reset the ball move distance and starting position.
        """
        self.x_move = BallConfig.MOVE_DISTANCE
        self.y_move = BallConfig.MOVE_DISTANCE
        self.goto(BallConfig.starting_position())
