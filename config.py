# default size of all objects
BASE_OBJECT_SIZE = 20

# game speed
GAME_SPEED = 0.02


class ScreenConfig:
    WIDTH = 800
    HEIGHT = 600
    BACKGROUND_COLOUR = "black"
    TITLE = "Break Out"


class PaddleConfig:
    SHAPE = "square"
    COLOUR = "white"
    STRETCH_LENGTH = 6
    MOVE_OFFSET = 15

    @classmethod
    def starting_position(cls) -> tuple[int, int]:
        """
        Return a tuple (x, y) representing the starting position of the paddle. 
        """
        return (0, -ScreenConfig.HEIGHT // 2 + 50)

    @classmethod
    def paddle_dimension(cls) -> tuple[int, int]:
        """
        Return a tuple (width, length) representing the dimensions of the paddle.
        """
        return (BASE_OBJECT_SIZE, BASE_OBJECT_SIZE * PaddleConfig.STRETCH_LENGTH)


class BallConfig:
    SHAPE = "circle"
    COLOUR = "white"
    MOVE_DISTANCE = 5
    BALL_RADIUS = BASE_OBJECT_SIZE // 2
    GAP = 1
    PADDLE_BOUNCE_FACTOR = 0.07
    SPEED_FACTOR = 1.02

    @classmethod
    def starting_position(cls) -> tuple[int, int]:
        """
        Return a tuple (x, y) representing the starting position of the ball. 
        """
        x, y = PaddleConfig.starting_position()
        return (x, y + BASE_OBJECT_SIZE)


class BrickConfig:
    SHAPE = "square"
    STRETCH_LENGTH = 3
    OFF_SCREEN_LOCATION = (10000, 10000)

    @classmethod
    def brick_dimension(cls) -> tuple[int, int]:
        """
        Return a tuple (width, length) representing the dimensions of a brick. 
        """
        return (BASE_OBJECT_SIZE, BASE_OBJECT_SIZE * BrickConfig.STRETCH_LENGTH)


class BrickFactoryConfig:
    ROWS = 8
    COLUMNS = 12
    GAP = 2  # empty space between bricks
    COLOURS = ["yellow"] * 2 + ["green"] * 2 + ["orange"] * 2 + ["red"] * 2
    POINTS = {"yellow": 1, "green": 3, "orange": 5, "red": 7}

    @classmethod
    def starting_position(cls) -> tuple[int, int]:
        """
        Return a tuple (x, y) representing the starting position of the first brick.
        """
        return (-ScreenConfig.WIDTH // 2, 75)


class ScoreBoardConfig:
    COLOUR = "white"
    LIVES = 3
    FONT = ("Arial", 20, "normal")

    @classmethod
    def location(cls) -> tuple[int, int]:
        """
        Return a tuple (x, y) representing the position of the scoreboard. 
        """
        return (0, ScreenConfig.HEIGHT // 2 - 35)
