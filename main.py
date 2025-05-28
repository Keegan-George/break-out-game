from config import *
from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from brick_factory import BrickFactory
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOUR)
screen.title("Break Out Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()
brick_factory = BrickFactory()
brick_factory.generate_bricks()

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

while scoreboard.lives and brick_factory.bricks:
    screen.update()
    sleep(BALL_SPEED)

    ball.move()

    if ball.has_gone_below_screen():
        scoreboard.lives -= 1
        scoreboard.update_score()
        ball.bounce_y()
        ball.goto(paddle.xcor(), paddle.ycor() + PADDLE_WIDTH)

    if ball.has_collided_with_upper_wall():
        ball.bounce_y()

    if ball.has_collided_with_side_wall():
        ball.bounce_x()

    if ball.has_collided_with_other_object(paddle):
        ball.bounce_y()

    for i in range(len(brick_factory.bricks) - 1, -1, -1):
        brick = brick_factory.bricks[i]
        if ball.has_collided_with_other_object(brick):
            scoreboard.score += 1
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
