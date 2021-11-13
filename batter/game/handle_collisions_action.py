from game.action import Action
from game.point import Point
from game import constants

class Handle_Collisions_Action(Action):
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service


    def execute(self, cast):
        if len(cast["ball"]) == 0:
            return
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        if self._physics_service.is_collision(paddle, ball):
            dx = ball.get_velocity_x()
            dy = (ball.get_velocity_y()) * -1
            ball.set_velocity(Point(dx,dy))
            self._audio_service.play_sound(constants.SOUND_BOUNCE)
        for brick in bricks:
            if self._physics_service.is_collision(brick, ball):
                dx = ball.get_velocity_x()
                dy = (ball.get_velocity_y()) * -1
                ball.set_velocity(Point(dx,dy))
                self._audio_service.play_sound(constants.SOUND_BOUNCE)
                cast["bricks"].remove(brick)

