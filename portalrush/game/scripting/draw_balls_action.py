from constants import *
from game.scripting.action import Action


class DrawBallsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        balls = cast.get_first_actor(BALLS_GROUP)
        body = balls.get_body()

        if balls.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)

        image = balls.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)
