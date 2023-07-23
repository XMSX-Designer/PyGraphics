class Rect:
    """
    A class representing a rectangle with position and size.

    Attributes:
        x (float): The x-coordinate of the top-left corner of the rectangle.
        y (float): The y-coordinate of the top-left corner of the rectangle.
        w (float): The width of the rectangle.
        h (float): The height of the rectangle.

    Methods:
        rect: Get the rectangle's position and size as a list.
        resize(scale=None, scale_to_width=None, scale_to_height=None, set_size=None): Resize the rectangle.
    """

    def __init__(self, x, y, w, h):
        """
        Initialize the Rect object with position and size.

        Args:
            x (float): The x-coordinate of the top-left corner of the rectangle.
            y (float): The y-coordinate of the top-left corner of the rectangle.
            w (float): The width of the rectangle.
            h (float): The height of the rectangle.
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    @property
    def rect(self):
        """
        Get the rectangle's position and size as a list.

        Returns:
            list: A list representing the rectangle's position and size in the format [x, y, w, h].
        """
        return [self.x, self.y, self.w, self.h]

    def resize(self, scale=None, scale_to_width=None, scale_to_height=None, set_size=None):
        """
        Resize the rectangle based on the provided scaling options or set a new size.

        Args:
            scale (float): Scale factor to resize the rectangle uniformly in both dimensions.
            scale_to_width (float): Scale factor to resize the rectangle to a specific width.
            scale_to_height (float): Scale factor to resize the rectangle to a specific height.
            set_size (tuple): Tuple (new_width, new_height) to set the new size of the rectangle.
        """
        w, h = self.w, self.h
        size = (w, h)

        if scale is not None:
            size = [round(w * scale), round(h * scale)]
        elif scale_to_width is not None:
            scale_factor = scale_to_width / w
            new_h = h * scale_factor
            size = [round(scale_to_width), round(new_h)]
        elif scale_to_height is not None:
            scale_factor = scale_to_height / h
            new_w = w * scale_factor
            size = [round(new_w), round(scale_to_height)]
        elif set_size is not None:
            nw, nh = set_size
            size = [round(nw), round(nh)]

        self.w, self.h = size
