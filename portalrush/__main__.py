from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager
import os  

def main():
    """Main function to start the game/program."""
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    """Runs the main if the file name is named as given."""
    main()