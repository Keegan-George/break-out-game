from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from brick_factory import BrickFactory
from scoreboard import ScoreBoard
from config import *

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

while scoreboard.lives and brick_factory.bricks:
    screen.update()
    sleep(BALL_SPEED)

    ball.move()

    if ball.is_below_screen():
        scoreboard.lives -= 1
        scoreboard.update_score()
        ball.bounce_y()
        ball.reset()
        ball.goto(paddle.xcor(), paddle.ycor() + PADDLE_WIDTH)

    if ball.has_hit_upper_wall():
        ball.bounce_y()

    if ball.has_hit_side_wall():
        ball.bounce_x()

    if ball.has_hit_other_object(paddle):
        ball.bounce_x_paddle(paddle)
        ball.bounce_y()

    for i in range(len(brick_factory.bricks) - 1, -1, -1):
        brick = brick_factory.bricks[i]
        if ball.has_hit_other_object(brick):
            scoreboard.score += brick.point
            scoreboard.update_score()
            ball.bounce_y()
            brick.remove()
            brick_factory.bricks.pop(i)
            break

if not scoreboard.lives:
    scoreboard.gameover()

if not brick_factory.bricks:
    scoreboard.winner()


screen.exitonclick()
