from game.directing.scene_manager import SceneManager
from game.directing.director import Director
#More Code TBU  


def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()
    #director = director #Dont run without removing this line

if __name__ == "__main__":
    main()
