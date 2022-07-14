import time
from constants import *
from game.scripting.action import Action



class TimeScoreAction(Action):
    
    def __init__(self, next_scene, delay):
        self._start = time.time()

    
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        elapsed = round(round(time.time() - self._start)) 
        elapsed = int(elapsed)
        stats.add_points(elapsed)
        
