import pyray
from game.casting.point import Point
from game.services.mouse_service import MouseService


class RaylibMouseService(MouseService):
    """ A Raylib implementation of MouseService."""

    def __init__(self):
        self._buttons = {}
        self._buttons["left"] = pyray.MOUSE_BUTTON_LEFT
        self._buttons["middle"] = pyray.MOUSE_BUTTON_MIDDLE
        self._buttons["right"] = pyray.MOUSE_BUTTON_RIGHT
    
    def get_coordinates(self):
        """get the position coordinate when moving
        
        Args:
            Self.
        """
        x = pyray.get_mouse_x()
        y = pyray.get_mouse_y()
        return Point(x, y)

    def has_mouse_moved(self):
        """Define the key control
        
        Args:
            key control of move and position.
        """
        mouse_delta = pyray.get_mouse_delta()
        return mouse_delta.x > 0 or mouse_delta.y > 0
    
    def is_button_down(self, button):
        """Define the key control
        
        Args:
            key control down with the raylib.
        """
        raylib_button = self._buttons[button]
        return pyray.is_mouse_button_down(raylib_button)
    
    def is_button_pressed(self, button):
        """Define the key control
        
        Args:
            key control pressed with raylib.
        """
        raylib_button = self._buttons[button]
        return pyray.is_mouse_button_pressed(raylib_button)
        
    def is_button_released(self, button):
        """Define the key control
        
        Args:
            key control release with raylib.
        """
        raylib_button = self._buttons[button]
        return pyray.is_mouse_button_released(raylib_button)
    
    def is_button_up(self, button):
        """Define the key control
        
        Args:
            key control up with raylib.
        """
        raylib_button = self._buttons[button]
        return pyray.is_mouse_button_up(raylib_button)
