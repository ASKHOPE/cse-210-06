from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
life = lives()
PLAYER_GROUP = 
OBSTACLE_GROUP = 



class CollideObstacleAction(Action):
    """Checks for the collision in the given argument of of player and the obstacle.
    
    Args : Action: The work which is done during the given time or the execution.
    """

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        obstacle = cast.get_actors(OBSTACLE_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for obstacle in obstacle:
            ball_body = player.get_body()
            obstacle_body = obstacle.get_body()

            if self._physics_service.has_collided(ball_body, obstacle_body):
                player.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = obstacle.get_points()
                stats.add_points(points)
                #cast.remove_actor(OBSTACLE_GROUP, obstacle) #Code to remove for points 
                lives= life - 1
                
                
                