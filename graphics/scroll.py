class VScroll:
    """
    A class representing a vertical scroll behavior for objects.

    Attributes:
        _objects (dict): A dictionary storing object IDs as keys and corresponding objects as values.
        _velocity (float): Current vertical scrolling velocity.
        _friction (float): Friction applied to the vertical scrolling velocity.
        _y (float): Current vertical position.
        upper (float): The upper limit of vertical scrolling.
        lower (float): The lower limit of vertical scrolling.

    Methods:
        addObject(id, obj): Add an object to the scrollable list.
        update(event): Update the vertical scrolling based on the provided event.
        set_friction(friction): Set the friction applied to the vertical scrolling velocity.
    """

    def __init__(self, upper, lower):
        """
        Initialize the VScroll object with upper and lower limits for vertical scrolling.

        Args:
            upper (float): The upper limit of vertical scrolling.
            lower (float): The lower limit of vertical scrolling.
        """
        self._objects = {}
        self._velocity = 0
        self._friction = 0.1
        self._y = 0
        self.upper = upper
        self.lower = lower

    def addObject(self, id, obj):
        """
        Add an object to the scrollable list.

        Args:
            id (str): Identifier for the object.
            obj (object): The object to be added to the scrollable list.
        """
        self._objects[str(id)] = obj

    def update(self, event):
        """
        Update the vertical scrolling based on the provided event.

        Args:
            event (Event): The event containing the mouse movement information.
        """
        relx, rely = event.mouse.rel
        new_y = 0
        first = True

        if event.mouse.press:
            new_y += rely
            if first:
                first = False
                self._y += rely
            self._velocity = rely
        else:
            new_y += self._velocity
            if first:
                first = False
                self._y += self._velocity
            self._velocity *= (1 - self._friction)

        for id, obj in self._objects.copy().items():
            oy = obj.yposition
            new_y2 = oy + new_y
            obj.yposition = new_y2

    def set_friction(self, friction):
        """
        Set the friction applied to the vertical scrolling velocity.

        Args:
            friction (float): The friction value to be set.
        """
        self._friction = friction
