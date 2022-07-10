import pathlib
from game.casting.color import Color

# GAME
GAME_NAME = "Portal Rush"
FRAME_RATE = 60 #Changes the smoothness of the game.

# SCREEN
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FONT
FONT_FILE = "cse-210-06/portalrush/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
COLLIDE_SOUND = "cse-210-06/portalrush/assets/sounds/boing.wav"
WELCOME_SOUND = "cse-210-06/portalrush/assets/sounds/start.wav"
OVER_SOUND = "cse-210-06/portalrush/assets/sounds/over.wav"


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
RIGHT = "right"
SPACE = "space"
ESCAPE = "escape"
PAUSE = "enter"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "To be Updated"
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
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# Player (Espiritu)
ESPIRITU_GROUP = "espiritu"
ESPIRITU_IMAGE = "cse-210-06/portalrush/assets/images/player.png"
ESPIRITU_WIDTH = 28
ESPIRITU_HEIGHT = 28
ESPIRITU_VELOCITY = 6

# Chaser (Reaper)
REAPER_GROUP = "reaper"
REAPER_IMAGES = "cse-210-06/portalrush/assets/images/reaper.png"
REAPER_WIDTH = 106
REAPER_HEIGHT = 28
REAPER_RATE = 6
REAPER_VELOCITY = 7

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS SPACE TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
