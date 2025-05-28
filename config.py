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
    MOVE_DISTANCE = 15

    @classmethod
    def starting_position(cls):
        return (0, -ScreenConfig.HEIGHT // 2 + 50)


class BallConfig:
    SHAPE = "circle"
    COLOUR = "white"
    MOVE_DISTANCE = 5
    BALL_RADIUS = DEFAULT_TURTLE_SIZE // 2

    @classmethod
    def starting_position(cls):
        x, y = PaddleConfig.starting_position()
        return (x, y + 20)
    

class BrickConfig:
    SHAPE = "square"
    STRETCH_LENGTH = 4


# paddle parameters
PADDLE_WIDTH = DEFAULT_TURTLE_SIZE

# ball parameters
BALL_SPEED = 0.02


# brick parameters
BRICK_WIDTH = DEFAULT_TURTLE_SIZE
BRICK_LENGTH = DEFAULT_TURTLE_SIZE * BRICK_STRETCH_LENGTH

# brick factory parameters
GAP_BETWEEN_BRICKS = 1
NUMBER_OF_ROWS = 8
NUMBER_OF_BRICKS_PER_ROW = ScreenConfig.SCREEN_WIDTH // (
    DEFAULT_TURTLE_SIZE * BRICK_STRETCH_LENGTH + GAP_BETWEEN_BRICKS
)
BRICKS_STARTING_X_POSITION = -ScreenConfig.SCREEN_WIDTH // 2
BRICKS_STARTING_Y_POSITION = 75

# scoreboard parameters
LIVES = 3
SCORE_DISTANCE_FROM_TOP = 35
SCORE_X_POSITION = 0
SCORE_Y_POSITION = ScreenConfig.SCREEN_HEIGHT // 2 - SCORE_DISTANCE_FROM_TOP
FONT = ("Arial", 20, "normal")
