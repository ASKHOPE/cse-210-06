from constants import *
from game.scripting.action import Action


class DrawReapertAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        reaper = cast.get_first_actor(REAPER_GROUP)
        body = reaper.get_body()

        if reaper.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = reaper.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)