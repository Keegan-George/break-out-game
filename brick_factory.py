from config import *
from brick import Brick


class BrickFactory:
    def __init__(self):
        self.bricks = []

    def generate_bricks(self):
        y_coordinate = BRICKS_STARTING_Y_POSITION

        for row in range(NUMBER_OF_ROWS):
            for column in range(NUMBER_OF_BRICKS_PER_ROW):
                brick = Brick()

                if row < 2:
                    brick.color("yellow")
                elif row < 4:
                    brick.color("green")
                elif row < 6:
                    brick.color("orange")
                else:
                    brick.color("red")

                x_coordinate = (
                    BRICKS_STARTING_X_POSITION
                    + BRICK_LENGTH / 2
                    + (
                        column
                        * (BASE_TURTLE_LENGTH + GAP_BETWEEN_BRICKS)
                        * BRICK_STRETCH_LENGTH
                    )
                )
                brick.goto(x_coordinate, y_coordinate)
                self.bricks.append(brick)

            y_coordinate += BRICK_WIDTH + GAP_BETWEEN_BRICKS
