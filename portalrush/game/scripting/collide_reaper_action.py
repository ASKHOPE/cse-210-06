from constants import *
from game.casting.stats import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideReaperAction(Action):
    def __init__(self,physics_service,audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self,cast,script,callback):
        reaper = cast.get_first_actor(REAPER_GROUP)
        player = cast.get_first_actor(PLAYER_GROUP)
        ground = cast.get_actors(GROUND_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        for ground in ground:
            reaper_body = reaper.get_body()
            ground_body = ground.get_body()
            #player_body = player.get_body()

     
            
        # if self._physics_service.has_collided(reaper_body,player_body):
        #     if stats.get_lives() == 1:
        #         stats.lose_life()
        #     else:
        #         print("Game OVER")

            
