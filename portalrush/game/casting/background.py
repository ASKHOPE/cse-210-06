from constants import *
from game.casting.actor import Actor

class Background(Actor):
    """A Background"""
    def __init__(self,body,image,debug=False):
        """Constructs a new Background."""

        super().__init__(debug)
        self._body = body
        self._image = image
        
    def get_body(self):
        """Gets the Balls body.

        Returns:
            An instance of Body.
        """
        return self._body
    
    def get_image(self):
        """Gets the images that make up the animation.

        Returns:
            A list of strings containing the image names.
        """
        return self._image