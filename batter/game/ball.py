from game.point import Point
from game.actor import Actor
from game import constants


class Ball(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(constants.BALL_WIDTH)
        self.set_height(constants.BALL_HEIGHT)
        self.set_image(constants.IMAGE_BALL)
        self.set_position(Point((constants.MAX_X /2) ,(constants.MAX_Y /3)*2))
        self.set_velocity(Point(1,1))
