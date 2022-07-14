from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Reaper(Actor):
    "The one who chases our players."
    def __init__(self,body,image,debug=False):
        super().__init__(debug)
        self._body = body
        self._image = image
    
    def get_body(self):
        """Gets the ball's body.
        
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

    def swing_right(self):
        """Runs Forward """
        
        position = self._body.get_position()
        self._body.set_position(position)
        
        velocity = Point(REAPER_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def move_next(self):
        """Moves the reaper using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def release(self):
        """Release the ball in a random direction."""
        # rn = random.uniform(0.9, 1.1)
        # rn= 5
        # vx = random.choice([-PLAYER_VELOCITY * rn, PLAYER_VELOCITY * rn])
        # vy = -PLAYER_VELOCITY
        velocity = Point(15, 0)  # vx =direction vy = Velocity
        self._body.set_velocity(velocity)
