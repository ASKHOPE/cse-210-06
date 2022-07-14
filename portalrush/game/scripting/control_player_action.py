from constants import *
from game.scripting.action import Action


class ControlPlayerAction(Action):
    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
    
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        if self._keyboard_service.is_key_down(LEFT):
            player.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT):
            player.swing_right()
        
        elif self._keyboard_service.is_key_down(D):
            player.swing_right()
            
        elif self._keyboard_service.is_key_down(A):
            player.swing_left()
    
      # Add delay to the else.In future.
        
        else:
            player.stop_moving()
            