from game.actor import Actor
from game import constants
from game.point import Point

class Paddle(Actor):
    """
    This is the Paddle it is used as the controlable 
    actor in the game
    """
    def __init__(self):
        super().__init__()
        self.set_bounce_on_edge(True)
        self.set_position(Point(constants.PADDLE_X,constants.PADDLE_Y))
        self.set_width(constants.PADDLE_WIDTH)
        self.set_height(constants.PADDLE_HEIGHT)
        self.set_image(constants.IMAGE_PADDLE)
        self.set_player_controlled(True)
        self.set_bounce_on_edge(True)
        self.set_type("paddle")
