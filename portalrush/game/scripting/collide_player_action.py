from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point



class CollidePlayerAction(Action):
    def __init__(self,physics_service,audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self,cast,script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        reaper = cast.get_first_actor(REAPER_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        ball = cast.get_first_actor(BALL_GROUP)
        ball_body = ball.get_body()

        reaper_body = reaper.get_body()
        player_body = player.get_body()
              

        if self._physics_service.has_collided(player_body, reaper_body):
            player = cast.get_first_actor(PLAYER_GROUP)
            sound = Sound(BONK_SOUND)
            self._audio_service.play_sound(sound)
            stats.lose_life()

            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN)
            else:
                callback.on_next(GAME_OVER)
                sound = Sound(OHNO_SOUND)
                self._audio_service.play_sound(sound)

       
          