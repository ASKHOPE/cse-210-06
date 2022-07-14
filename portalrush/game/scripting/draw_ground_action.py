from constants import *
from game.scripting.action import Action

class DrawGroundAction(Action):
    def __init__(self,video_service):
        self._video_service = video_service
        
    def execute(self,cast,script,callback):
        ground = cast.get_actors(GROUND_GROUP)
        for ground in ground:
            body = ground.get_body()
            
            if ground.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
            
            image = ground.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
