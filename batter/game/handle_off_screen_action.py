from game.action import Action
from game.point import Point
from game import constants

class Handle_Off_Screen_Action(Action):
    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if actor.get_bounce_on_edge():
                    if actor.get_position_y() < 0:
                        dx = actor.get_velocity_x()
                        dy = (actor.get_velocity_y()) * -1
                        actor.set_velocity(Point(dx,dy))
                    if actor.get_position_x() + actor.get_width() > constants.MAX_X or actor.get_position_x() < 0:
                        dx = (actor.get_velocity_x()) * -1
                        dy = actor.get_velocity_y()
                        actor.set_velocity(Point(dx,dy))
                if actor.get_position_y() > constants.MAX_Y:
                    cast["ball"].remove(actor)