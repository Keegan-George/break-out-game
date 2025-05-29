# default length of a turtle object
DEFAULT_TURTLE_SIZE = 20


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
    def starting_position(cls):
        return (0, -ScreenConfig.HEIGHT // 2 + 50)


class BallConfig:
    SHAPE = "circle"
    COLOUR = "white"
    MOVE_DISTANCE = 5
    BALL_RADIUS = DEFAULT_TURTLE_SIZE // 2
    GAP = 1
    BOUNCE_FACTOR = 0.07

    @classmethod
    def starting_position(cls):
        x, y = PaddleConfig.starting_position()
        return (x, y + 20)


class BrickConfig:
    SHAPE = "square"
    STRETCH_LENGTH = 3


class BrickFactoryConfig:
    ROWS = 8
    COLUMNS = 12
    GAP = 2  # empty space between bricks
    COLOURS = ["yellow"] * 2 + ["green"] * 2 + ["orange"] * 2 + ["red"] * 2
    POINTS = {"yellow": 1, "green": 3, "orange": 5, "red": 7}

    @classmethod
    def starting_position(cls):
        return (-ScreenConfig.WIDTH // 2, 75)


class ScoreBoardConfig:
    COLOUR = "white"
    LIVES = 3
    FONT = ("Arial", 20, "normal")

    @classmethod
    def location(cls):
        return (0, ScreenConfig.HEIGHT // 2 - 35)


# paddle parameters
PADDLE_WIDTH = DEFAULT_TURTLE_SIZE

# ball parameters
BALL_SPEED = 0.02
