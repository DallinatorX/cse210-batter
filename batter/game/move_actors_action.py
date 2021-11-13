from game.action import Action
from game.point import Point
#from game import constants

class Move_Actors_Action(Action):
    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                x = actor._position.get_x()
                y = actor._position.get_y()
                dx = actor._velocity.get_x()
                dy = actor._velocity.get_y()
                x = (x + dx) #% constants.MAX_X
                y = (y + dy) #% constants.MAX_Y

                position = Point(x, y)
                actor.set_position(position)
