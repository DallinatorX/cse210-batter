from game.action import Action
from game.input_service import InputService
from game.point import Point
from game import constants

class Control_Actors_Action(Action):
    def __init__(self):
        self._input_service = InputService()


    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if actor.is_player_controlled():
                    if self._input_service.is_left_pressed():
                        actor.set_velocity(Point(-constants.PADDLE_SPEED,0))
                    elif self._input_service.is_right_pressed():
                        actor.set_velocity(Point(constants.PADDLE_SPEED,0))
                    else:
                        actor.set_velocity(Point(0,0))