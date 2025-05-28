from brick import Brick
from config import BrickConfig, BrickFactoryConfig, DEFAULT_TURTLE_SIZE


class BrickFactory:
    def __init__(self):
        self.bricks: list[Brick] = []

    def generate_brick_wall(self):
        """
        Generates the rows of bricks that form a brick wall. 
        
        """
        x_start, y_start = BrickFactoryConfig.starting_position()
        brick_length = DEFAULT_TURTLE_SIZE * BrickConfig.STRETCH_LENGTH

        for row in range(BrickFactoryConfig.ROWS):
            x_coordiante = x_start

            for column in range(BrickFactoryConfig.COLUMNS):
                x_coordiante += BrickFactoryConfig.GAP + brick_length 
                brick = self.create_brick(x_coordiante, y_start, BrickFactoryConfig.COLOURS[row])
                self.bricks.append(brick)

            y_start += DEFAULT_TURTLE_SIZE + BrickFactoryConfig.GAP


    def create_brick(self, x: int, y: int, colour: str) -> Brick:
        """
        Returns a new Brick with the given coordinates and colour. 
        """
        brick = Brick()
        brick.color(colour)
        brick.goto(x, y)
        return brick
