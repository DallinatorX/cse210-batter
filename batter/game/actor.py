from game import constants
from game.point import Point

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
        _width (int): The actor's width
        _height (int): The actor's height
        _image (string): The file path of the image file (if present)
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Actor): an instance of Actor.
        """
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._width = 0
        self._height = 0
        self._image = ""
        self._bounce_on_edge = False
        self._player_controlled = False
        self._type = ""

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
    
    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_image(self):
        return self._image
    
    def set_image(self, image):
        self._image = image

    def get_left_edge(self):
        return self._position.get_x()

    def get_right_edge(self):
        return self._position.get_x() + self._width

    def get_top_edge(self):
        return self._position.get_y()

    def get_bottom_edge(self):
        return self._position.get_y() + self._height

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def get_position_x(self):
        return self._position.get_x()

    def get_position_y(self):
        return self._position.get_y()

    def get_text(self):
        """Gets the actor's textual representation.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def set_text(self, text):
        self._text = text;

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def get_velocity_x(self):
        return self._velocity.get_x()

    def get_velocity_y(self):
        return self._velocity.get_y()
    
    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            self (Actor): An instance of Actor.
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given velocity.
        """
        self._velocity = velocity

    def has_text(self):
        return self._text != ""

    def has_image(self):
        return self._image != ""

    def set_bounce_on_edge(self,bounce):
        self._bounce_on_edge = bounce

    def get_bounce_on_edge(self):
        return self._bounce_on_edge

    def is_player_controlled(self):
        return self._player_controlled

    def set_player_controlled(self, controlled):
        self._player_controlled = controlled

    def set_type(self, kind):
        self._type = kind

    def get_type(self):
        return self._type