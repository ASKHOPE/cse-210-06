from constants import *
from game.casting.actor import Actor

class Background(Actor):
    def __init__(self,body,image,debug=False):
        super().__init__(debug)
        self._body = body
        self._image = image
        
    def get_body(self):
        return self._body
    
    def get_image(self):
        return self._image