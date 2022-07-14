import csv
from constants import *
from game.casting.animation import Animation
from game.casting.ball import Ball
from game.casting.balls import Balls

from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point

from game.casting.player import Player
from game.casting.ground import Ground
from game.casting.reaper import Reaper
from game.casting.background import Background


# GENERAL GAME FILES #
from game.casting.stats import Stats
from game.casting.text import Text
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.time_score_action import TimeScoreAction

#Collision Imports
from game.scripting.collide_borders_action import CollideBordersAction # Add this code to make the player bounce jump of walls
from game.scripting.collide_ball_action import CollideBallAction
from game.scripting.collide_player_action import CollidePlayerAction
from game.scripting.collide_reaper_action import CollideReaperAction

#Control Imports
from game.scripting.control_player_action import ControlPlayerAction

#Draw Imports
from game.scripting.draw_ball_action import DrawBallAction
from game.scripting.draw_balls_action import DrawBallsAction
from game.scripting.draw_player_action import DrawPlayerAction
from game.scripting.draw_reaper_action import DrawReaperAction
from game.scripting.draw_ground_action import DrawGroundAction
from game.scripting.draw_background_action import DrawBackgroundAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.end_drawing_action import EndDrawingAction

#Player Movement Imports
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_balls_action import MoveBallsAction
from game.scripting.move_player_action import MovePlayerAction

#Game Working Imports
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction

#Ray Lib Imports
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    
    #Collision Code 
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE) #USe this code to enhance the game
    COLLIDE_REAPER_ACTION =CollideReaperAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_PLAYER_ACTION = CollidePlayerAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    TIME_SCORE_ACTION = TimeScoreAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_BALL_ACTION = CollideBallAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    
    
    #Control Code
    CONTROL_PLAYER_ACTION = ControlPlayerAction(KEYBOARD_SERVICE)
    #CONTROL_GROUND_ACTION = ControlGroundAction(KEYBOARD_SERVICE)
    # #Draw Variables Code
    DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    DRAW_BALLS_ACTION = DrawBallsAction(VIDEO_SERVICE)

    DRAW_PLAYER_ACTION = DrawPlayerAction(VIDEO_SERVICE)
    DRAW_REAPER_ACTION = DrawReaperAction(VIDEO_SERVICE)
    DRAW_GROUND_ACTION = DrawGroundAction(VIDEO_SERVICE)
    DRAW_BACKGROUND_ACTION = DrawBackgroundAction(VIDEO_SERVICE)
          
    #Move Variable Code
    MOVE_PLAYER_ACTION = MovePlayerAction()
    MOVE_BALL_ACTION = MoveBallAction()
    MOVE_BALLS_ACTION = MoveBallsAction()
    
    #General Score and Lives Code
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)

    #Game Ray Lib services
    
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)    
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_ball(cast)
        self._add_balls(cast)
        self._add_reaper(cast)
        self._add_player(cast)
        self._add_ground(cast)
        self._add_background(cast)


        self._add_dialog(cast, SPACE_TO_START) # ENTER TO START can be changeable

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_ball(cast)
        self._add_balls(cast)
        self._add_reaper(cast)
        self._add_player(cast)
        self._add_ground(cast)
        self._add_background(cast)


        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 4))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_ball(cast)
        self._add_balls(cast)
        self._add_player(cast)
        self._add_score(cast)
        # self._add_racket(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 3))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):#CONTROLS THE PLAYER IN THE ACUTAL GAME
        self._activate_ball(cast)
        self._activate_balls(cast)

       

        cast.clear_actors(DIALOG_GROUP)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_PLAYER_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_ball(cast)
        self._add_ball(cast)
        self._add_reaper(cast)
        self._add_player(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)
    
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)
        
    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        ball.release()
        
    def _activate_balls(self, cast):
        balls = cast.get_first_actor(BALLS_GROUP)
        balls.release()
    

    def _add_ball(self, cast) :
        cast.clear_actors(BALL_GROUP)
        x = 175
        y = 310
        
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        size = position
        velocity = Point(0, 0)
 
        body = Body(position, size, velocity)

        image = Image(BALL_IMAGE)
        ball = Ball(body, image)
        cast.add_actor(BALL_GROUP, ball)

    def _add_balls(self, cast):
        cast.clear_actors(BALLS_GROUP)
        x = 175
        y = 310
        position = Point(x, y)
        size = Point(BALLS_WIDTH, BALLS_HEIGHT)
        size = position
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALLS_IMAGE)
        balls = Balls(body, image)
        cast.add_actor(BALLS_GROUP, balls)
        
    # TWEAK THIS CODE TO SPAWN GROUNDS ON THE ROAD USING RANDOM VARIABLES

    def _add_ground(self, cast):
        # cast.clear_actors(BRICK_GROUP)

        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):

                    x = FIELD_LEFT + c * GROUND_WIDTH  # Ground spawn coordinates
                    y = FIELD_TOP + r * GROUND_HEIGHT
                    color = column[0]
                    frames = int(column[1])
                    # points = GROUND_POINTS
                    # if frames == 1:
                    #     points *= 2
                    position = Point(x, 400)  # Floor co ordinates
                    size = Point(GROUND_WIDTH, GROUND_HEIGHT)
                    velocity = Point(0, 0)
                    # images = GROUND_IMAGES[color][0:frames]
                    body = Body(position, size, velocity)
                    # animation = Animation(images, GROUND_RATE, GROUND_DELAY)
                    image = Image(GROUND_IMAGE)
                    # brick = Brick(body, animation, points)
                    ground = Ground(body, image, True)
                    cast.add_actor(GROUND_GROUP, ground)


    
    def _add_background(self, cast):
        cast.clear_actors(BACKGROUND_GROUP)
        position = Point(FIELD_TOP_LEFT, FIELD_LEFT) # X,Y
       # size = Point(BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
        size = position
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BACKGROUND_IMAGE)
        background = Background(body, image, True)
        cast.add_actor(BACKGROUND_GROUP, background)


    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)


    def _add_reaper(self,cast):
        cast.clear_actors(REAPER_GROUP)
        x = CENTER_XX / 1.7 - REAPER_WIDTH  #Fiddle with 1.7 (Far) and 1.5  (Close)
        y = SCREEN_HEIGHT-70 - REAPER_HEIGHT
        position = Point(x,y)
        size = Point(REAPER_WIDTH, REAPER_HEIGHT)
        velocity = Point(0,0)
        body = Body(position,size,velocity)
        image = Image(REAPER_IMAGE)
        reaper = Reaper(body, image)
        cast.add_actor(REAPER_GROUP , reaper)
        
        
    def _add_player(self, cast):
        cast.clear_actors(PLAYER_GROUP)
        # x = CENTER_XX - PLAYER_WIDTH / 2
        # y = SCREEN_HEIGHT-REAPER_HEIGHT / 1.96 - PLAYER_HEIGHT
        
        x= 700
        y = 303
        position = Point(x, y)
        size = Point(PLAYER_WIDTH, PLAYER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(PLAYER_IMAGE)
        player = Player(body, image)
        cast.add_actor(PLAYER_GROUP, player)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        
        # DO NOT CHANGE THIS ORDER
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_BACKGROUND_ACTION)

        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)

        script.add_action(OUTPUT, self.DRAW_REAPER_ACTION)

        script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        script.add_action(OUTPUT, self.DRAW_BALLS_ACTION)


        script.add_action(OUTPUT, self.DRAW_GROUND_ACTION)
        script.add_action(OUTPUT, self.DRAW_PLAYER_ACTION)
        

        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)
        
        
    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        # DO NOT CHANGE THIS ORDER

        script.clear_actions(UPDATE)

        script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        script.add_action(UPDATE, self.MOVE_BALLS_ACTION)

        script.add_action(UPDATE, self.MOVE_PLAYER_ACTION)


        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BALL_ACTION)
        script.add_action(UPDATE, self.COLLIDE_REAPER_ACTION)
        script.add_action(UPDATE, self.COLLIDE_PLAYER_ACTION)
        
        # UPDATE WALL BOUNCES DONE
        script.add_action(UPDATE, self.TIME_SCORE_ACTION)

        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
