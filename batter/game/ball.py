from game.point import Point
from game.actor import Actor
from game import constants


class Ball(Actor):
    """
    This is the ball actor that is used in the game
    """
    def __init__(self):
        super().__init__()
        self.set_width(constants.BALL_WIDTH)
        self.set_height(constants.BALL_HEIGHT)
        self.set_image(constants.IMAGE_BALL)
        self.set_position(Point(constants.BALL_X ,constants.BALL_Y))
        self.set_velocity(Point(constants.BALL_DX,constants.BALL_DY * -1))
        self.set_bounce_on_edge(True)
        self.set_type("ball")
