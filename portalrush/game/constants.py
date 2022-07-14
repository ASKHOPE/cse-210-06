import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Portal Rush"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
CENTER_X = SCREEN_WIDTH / 2
CENTER_XX = SCREEN_WIDTH / 3 #one third distance horizontally

CENTER_Y = SCREEN_HEIGHT / 2
CENTER_YY = SCREEN_HEIGHT / 3 #one third distance vertically


# FIELD
FIELD_TOP_LEFT = 0
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_FLOOR = 380
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "batter/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "batter/assets/sounds/boing.wav"
WELCOME_SOUND = "batter/assets/sounds/intro.mp3"
OVER_SOUND = "batter/assets/sounds/over.wav"
OUCH_SOUND = "batter/assets/sounds/ouch.mp3"
OHNO_SOUND = "batter/assets/sounds/ohno.mp3"
BONK_SOUND = "batter/assets/sounds/bonk.mp3"
#WELCOME_SOUND = "batter/assets/sounds/retro.mp3"


# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
A = "a"
D = "d"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"


# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "batter/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 20
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: INFINITE"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALLS
BALLS_GROUP = "balls"
BALLS_IMAGE = "batter/assets/images/0000.png"
BALLS_WIDTH = 18
BALLS_HEIGHT = 18
BALLS_VELOCITY = 6

# BALL
BALL_GROUP = "ball"
BALL_IMAGE = "batter/assets/images/000.png"
BALL_WIDTH = 18
BALL_HEIGHT = 18
BALL_VELOCITY = 10

#Background 
BACKGROUND_GROUP = "background"
BACKGROUND_IMAGE = "batter/assets/images/background.png"
BACKGROUND_WIDTH = 1000
BACKGROUND_HEIGHT = 500

# Player
PLAYER_GROUP = "player"
PLAYER_IMAGE = "batter/assets/images/player.png"
PLAYER_WIDTH = 68
PLAYER_HEIGHT = 100
PLAYER_RATE = 60
PLAYER_VELOCITY = 6


#Reaper 
REAPER_GROUP = "reaper"
REAPER_IMAGE = "batter/assets/images/reaper.png"
REAPER_WIDTH = 165
REAPER_HEIGHT = 190
REAPER_VELOCITY = 8

#Floor
GROUND_GROUP = "ground"
GROUND_IMAGE = "batter/assets/images/ground.png"
GROUND_WIDTH = 50
GROUND_HEIGHT = 100
GROUND_VELOCITY = 6



# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
SPACE_TO_START = "PRESS SPACE TO START \n A or <- to move LEFT \n D or -> to move RIGHT"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH \n Don't Get Caught or Hit"
WAS_GOOD_GAME = "GAME OVER"