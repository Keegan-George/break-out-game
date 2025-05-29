from turtle import Screen
from ball import Ball
from paddle import Paddle
from time import sleep
from brick import Brick
from brick_factory import BrickFactory
from scoreboard import ScoreBoard
from config import *


class Game:
    def __init__(self):
        self.screen, self.paddle, self.ball, self.brick_factory, self.scoreboard = (
            self.initialize_game()
        )

    def play(self):
        self.play_game(
            self.screen, self.paddle, self.ball, self.brick_factory, self.scoreboard
        )

    def initialize_game(self) -> tuple[Screen, Paddle, Ball, BrickFactory, ScoreBoard]:
        """Initialize the game and components."""
        screen = Screen()
        screen.setup(width=ScreenConfig.WIDTH, height=ScreenConfig.HEIGHT)
        screen.bgcolor(ScreenConfig.BACKGROUND_COLOUR)
        screen.title(ScreenConfig.TITLE)
        screen.tracer(0)

        paddle = Paddle()
        ball = Ball()
        scoreboard = ScoreBoard()
        brick_factory = BrickFactory()
        brick_factory.generate_brick_wall()

        screen.listen()
        screen.onkeypress(lambda: paddle.move("left"), "Left")
        screen.onkeypress(lambda: paddle.move("right"), "Right")

        return screen, paddle, ball, brick_factory, scoreboard

    def play_game(
        self,
        screen: Screen,
        paddle: Paddle,
        ball: Ball,
        brick_factory: BrickFactory,
        scoreboard: ScoreBoard,
    ) -> None:
        """
        Starts the game.
        """
        while scoreboard.lives and brick_factory.bricks:
            screen.update()
            sleep(GAME_SPEED)

            ball.move()

            # ball below screen
            if ball.is_below_screen():
                scoreboard.lives -= 1
                scoreboard.refresh_scoreboard()
                ball.bounce_y()
                ball.reset()

            # ball collision with upper hall
            if ball.has_hit_upper_wall():
                ball.bounce_y()

            # ball collision with side wall
            if ball.has_hit_side_wall():
                ball.bounce_x()

            # ball collision with paddle
            if ball.has_hit_other_object(paddle):
                ball.bounce_x_paddle(paddle)
                ball.bounce_y()

            # ball collision with brick
            hit_brick: Brick = next(
                (
                    brick
                    for brick in brick_factory.bricks
                    if ball.has_hit_other_object(brick)
                ),
                None,
            )
            if hit_brick:
                scoreboard.score += hit_brick.point
                scoreboard.refresh_scoreboard()
                ball.bounce_y()
                hit_brick.remove()
                brick_factory.bricks.remove(hit_brick)

        if not scoreboard.lives:
            scoreboard.display_message("GAME OVER")

        if not brick_factory.bricks:
            scoreboard.display_message("YOU WIN")

        screen.exitonclick()
