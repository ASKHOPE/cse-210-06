import pyray
from game.services.keyboard_service import KeyboardService


class RaylibKeyboardService(KeyboardService):
    """A Raylib implementation of KeyboardService."""

    def __init__(self):
        self._keys = {}
        self._keys["a"] = pyray.KEY_A
        self._keys["d"] = pyray.KEY_D
        self._keys["s"] = pyray.KEY_S
        self._keys["w"] = pyray.KEY_W

        self._keys["h"] = pyray.KEY_H
        self._keys["left"] = pyray.KEY_LEFT
        self._keys["right"] = pyray.KEY_RIGHT
        self._keys["up"] = pyray.KEY_UP
        self._keys["down"] = pyray.KEY_DOWN
        self._keys["enter"] = pyray.KEY_ENTER
        self._keys["space"] = pyray.KEY_SPACE

    def is_key_down(self, key):
        """Define the key control
        
        Args:
            key control of the down move and position.
        """
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_down(raylib_key)
    
    def is_key_pressed(self, key):
        """Define the key control
        
        Args:
            key control of when pressing the keyboard.
        """
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_pressed(raylib_key)
    
    def is_key_released(self, key):
        """Define the key control
        
        Args:
            key control of the release move.
        """
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_released(raylib_key)
    
    def is_key_up(self, key):
        """Define the key control
        
        Args:
            key control of the up move and position.
        """
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_up(raylib_key)
