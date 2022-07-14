from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Player(Actor):
    "PLayer who is gonna jump"
    def __init__(self,body,image,debug=False):
        super().__init__(debug)
        self._body = body
        self._image = image
        #self._position = position
        
    def get_image(self):
        """Gets the image of player.
        
        Returns:
            An instance of Image.
        """
        return self._image    
    
    def get_body(self):
        """Gets the ball's body.
        Returns:
            An instance of Body.
        """
        return self._body
    
    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Runs Back """
        # position = self._body.get_position()
        # self._body.set_position(position)

        velocity = Point(-PLAYER_VELOCITY, 0)
        self._body.set_velocity(velocity)
        

    def swing_right(self):
        """Runs Forward """
        velocity = Point(PLAYER_VELOCITY, 0)
        self._body.set_velocity(velocity)
  
        
    def stop_moving(self):
        """Stops the player from moving."""
        # position = self._body.get_position()
        # position = Point(position._x, position._y)
        # self._body.set_position(position)
        
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
        
     
    #FUTURE DEVELOPEMENT IDEAS    
        
    # def release(self):
    #     """Release the ball in a random direction."""
    #     # rn = random.uniform(0.9, 1.1)
    #     # rn= 5
    #     # vx = random.choice([-PLAYER_VELOCITY * rn, PLAYER_VELOCITY * rn])
    #     # vy = -PLAYER_VELOCITY
    #     velocity = Point(15, 0) #vx =direction vy = Velocity 
    #     self._body.set_velocity(velocity)
    
    # def jump_up(self):
    #     "Jump Up"
    #     position = self._body.get_position()

    #     #velocity = Point(0,-60)
    #     #self._body.set_velocity(velocity)
    #     position = Point(position._x, 200)
    #     self._body.set_position(position)

    # def on_ground(self):
    #     "Makes Runner fall down"
    #     position = self._body.get_position()
    #     position = Point(position._x, 300)
    #     self._body.set_position(position)
    #    # self._body.set_velocity(velocity)
    #     #self._body.set_velocity(velocity)
