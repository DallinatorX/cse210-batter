from random import randint
from game.actor import Actor
from game import constants

class Brick(Actor):
    """
    This class holds the info needed for storing the bricks
    """
    def __init__(self):
        super().__init__()
        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)
        self.set_image(constants.IMAGE_BRICK[randint(0,6)])
        self.set_type("brick")