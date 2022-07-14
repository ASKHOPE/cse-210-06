# from portalrushs.constants import GROUND_VELOCITY
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Ground(Actor):
    "Grounds to make player stumble"

    def __init__(self, body, image, debug=False):
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_image(self):
        return self._image

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Runs Back """
        velocity = Point(GROUND_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the ball's body.

          Returns:
        An instance of Body.
        """
        return self._body

    #FUTURE WORKINGS
    # def release(self):
    #     """Release the ball in a random direction."""
    #     # rn = random.uniform(0.9, 1.1)
    #     # rn= 5
    #     # vx = random.choice([-PLAYER_VELOCITY * rn, PLAYER_VELOCITY * rn])
    #     # vy = -PLAYER_VELOCITY
    #     velocity = Point(0, 0)  # vx =direction ,vy = Velocity ,x=15
    #     self._body.set_velocity(velocity)
