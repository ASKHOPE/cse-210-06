import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Balls(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Second Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def bounce_x(self):
        """Bounces the Balls in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.8, 1)
        #rn = 0
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the Balls in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.8, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the Balls body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the Balls image.
        
        Returns:
            An instance of Image.
        """
        return self._image
    
    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)
    
        
    def release(self):
        """Release the BALLSS in a random direction."""
        rn = random.uniform(0.8, 1.1)
        vx = random.choice([-BALLS_VELOCITY * rn, BALLS_VELOCITY * rn])
        vy = -BALLS_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)