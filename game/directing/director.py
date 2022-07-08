import pyray
from constants import *
from game.casting.cast import Cast
from game.directing.scene_manager import SceneManager
from game.scripting.action_callback import ActionCallback
from game.scripting.script import Script


class Director(ActionCallback):
    """A person who directs the game."""

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.

        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._cast = Cast()
        self._script = Script()
        self._scene_manager = SceneManager()

    def on_next(self, scene):
        """Overriden ActionCallback method transitions to next scene.

        Args:
            A number representing the next scene to transition to.
        """
        self._scene_manager.prepare_scene(scene, self._cast, self._script)

    def start_game(self):
        """Starts the game. Runs the main game loop."""
        self.on_next(NEW_GAME)
        self._execute_actions(INITIALIZE)
        self._execute_actions(LOAD)
        while self._video_service.is_window_open():
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)
        self._execute_actions(UNLOAD)
        self._execute_actions(RELEASE)

    def _execute_actions(self, group):
        """Calls execute for each action in the given group.

        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)
        for action in actions:
            action.execute(self._cast, self._script, self)

    def __init__(self, keyboard_service, display_service):
        self.__game_over = False
        """Constructs a new Director using the specified keyboard and display services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            display_service (DisplayService): An instance of DisplayService.
        """
        self._keyboard_service = keyboard_service
        self._display_service = display_service

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._display_service.open_window()
        self._init_t = time.perf_counter()  # Set the initial time counter
        self._enemy_t = time.perf_counter()  # Set the initial enemy time counter
        self._enemy_rate = 3  # Enemies will appear each 3 seconds

        run = True
        quit_game = False
        frame_duration = self._display_service.get_frame_duration()

        while run:
            # This line determines the time of each frame (actually it says to the program to wait a certain amout of time before executing the next steps).
            pyray.time.delay(frame_duration)
            for event in pyray.event.get():
                # If player press the window X set quit_game to true and stops this loop
                if event.type == pyray.QUIT:
                    pyray.mixer.music.fadeout(1000 * 2)
                    pyray.mixer.music.unload()

                    run = False
                    quit_game = True
                    pyray.mixer.music.load(TITLE_MUSIC)
                    pyray.mixer.music.play(-1)

            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
            if self._is_over():
                pyray.mixer.music.fadeout(1000 * 2)
                pyray.mixer.music.unload()
                run = False
                pyray.mixer.music.load(TITLE_MUSIC)
                pyray.mixer.music.play(-1)

        # If the player had pressed X before then quit_game will be true and the game over message won't be displayed.
        if not quit_game:
            game_over_message = Banner(Point(0, 0), 'Game Over', 60)
            max_x = self._display_service.get_width()
            max_y = self._display_service.get_height()
            game_over_message.set_center(Point(max_x / 2, max_y / 2))
            cast.add_actor("game_over_message", game_over_message)

            run = True
            while run:
                # This new loop don't get new inputs neither do new updates (so the game "freezes")
                pyray.time.delay(frame_duration)
                self._do_outputs(cast)
                # If the player press the window X this loop stops
                for event in pyray.event.get():
                    if event.type == pyray.QUIT:
                        run = False
