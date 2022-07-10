from constants import *
from game.scripting.action import Action


class MoveEspirituAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        espiritu = cast.get_first_actor(ESPIRITU_GROUP)
        body = espiritu.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
