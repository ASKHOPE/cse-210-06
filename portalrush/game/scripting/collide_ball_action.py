from calendar import c
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point


class CollideBallAction(Action):
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        #self._body = player.get_body()
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        ball = cast.get_first_actor(BALL_GROUP)
        balls = cast.get_first_actor(BALLS_GROUP)
        ouch_sound = Sound(OUCH_SOUND,0.1)

        ball_body = ball.get_body()
        ball_position = ball_body.get_position()
        
        balls_body = balls.get_body()
        balls_position = balls_body.get_position()
        
        player_body = player.get_body()
        player_position = player_body.get_position()
        # print(player_position.get_y())
        # print(player_position.get_x())

        #print(ball_position.get_x())
        #print(ball_position.get_y())
        x1 = player_position.get_x() #Horitontal --
        y1 = player_position.get_y() #Vertical |
        xr = x1 + 68
        yr = y1 + 100
        
        
        x2 = ball_position.get_x()  # Horitontal --
        y2 = ball_position.get_y()  # Vertical |
        
        x3 = balls_position.get_x() # Horitontal
        y3 = balls_position.get_y() # Vertical |
        
        
        y2= round(float(y2))
        # print(y2)
        x2 = round(float(x2))
        # print(x2)
        
        x3= round(float(x3))
        y3= round(float(y3))
        
        if y3 in range(y1, yr) and x3 in range(x1, xr):
            self._audio_service.play_sound(ouch_sound)
            stats.lose_life()

            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN)
            else:
                callback.on_next(GAME_OVER)
                sound = Sound(OVER_SOUND)
                self._audio_service.play_sound(sound)

        elif y2 in range(y1,yr) and x2 in range(x1,xr):
           # print("Hit")
            self._audio_service.play_sound(ouch_sound)
            stats.lose_life()

            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN)
            else:
                callback.on_next(GAME_OVER)
                sound = Sound(OVER_SOUND)
                self._audio_service.play_sound(sound)
         
        #FUTURE WORKS        
        # elif y2 == y3 and x2 == x3:
        #     balls.bounce_y()
        #     ball.bounce_x()
            
        

        # if self._physics_service.has_collided(player_position._x, ball_position._x):
        #   self._audio_service.play_sound(bounce_sound)
