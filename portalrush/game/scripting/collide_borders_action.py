from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        balls = cast.get_first_actor(BALLS_GROUP)

        body1 = balls.get_body()
        body = ball.get_body()
        position = body.get_position()
        position1 =body1.get_position()
        x = position.get_x()
        y = position.get_y()
        x1 = position1.get_x()
        y1 = position1.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)
               
               
    #BALL ONE 
        if x < FIELD_LEFT:
            ball.bounce_x()
           # self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball.bounce_x()
           # self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball.bounce_y()
           # self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_FLOOR - BALL_WIDTH):
            ball.bounce_y()
            
            
    #BALL TWO
        if x1 < FIELD_LEFT:
            balls.bounce_x()
            #self._audio_service.play_sound(bounce_sound)

        elif x1 >= (FIELD_RIGHT - BALL_WIDTH):
            balls.bounce_x()
           # self._audio_service.play_sound(bounce_sound)

        if y1 < FIELD_TOP:
            balls.bounce_y()
            #self._audio_service.play_sound(bounce_sound)

        elif y1 >= (FIELD_FLOOR- BALL_WIDTH):
            balls.bounce_y()

