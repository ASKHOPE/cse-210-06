from constants import *
from game.scripting.action import Action


class DrawEspirituAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        espiritu = cast.get_first_actor(ESPIRITU_GROUP)
        body = espiritu.get_body()

        if espiritu.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = espiritu.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)