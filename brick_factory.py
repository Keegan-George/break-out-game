from brick import Brick
from config import BrickConfig, BrickFactoryConfig


class BrickFactory:
    def __init__(self):
        self.bricks: list[Brick] = []

    def generate_brick_wall(self) -> None:
        """
        Generates the rows of bricks that form the brick wall.
        """
        x_start, y_start = BrickFactoryConfig.starting_position()
        brick_width, brick_length = BrickConfig.brick_dimension()

        for row in range(BrickFactoryConfig.ROWS):
            x_coordinate = x_start

            for _ in range(BrickFactoryConfig.COLUMNS):
                x_coordinate += BrickFactoryConfig.GAP + brick_length
                brick = self.create_brick(
                    x_coordinate, y_start, BrickFactoryConfig.COLOURS[row]
                )
                self.bricks.append(brick)

            y_start += brick_width + BrickFactoryConfig.GAP

    def create_brick(self, x: int, y: int, colour: str) -> Brick:
        """
        Returns a new Brick with the given coordinates and colour.
        """
        brick = Brick()
        brick.color(colour)
        brick.point = BrickFactoryConfig.POINTS[colour]
        brick.goto(x, y)
        return brick
