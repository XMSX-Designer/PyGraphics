from win32api import GetSystemMetrics

class Display:
    """
    A class representing display information and providing a static method to get the screen size.

    Methods:
        get_size(): Get the screen size as a tuple (width, height).
    """

    @staticmethod
    def get_size():
        """
        Get the screen size using the GetSystemMetrics function from the win32api library.

        Returns:
            tuple: A tuple containing the screen width and height in pixels.
        """
        return GetSystemMetrics(0), GetSystemMetrics(1)
