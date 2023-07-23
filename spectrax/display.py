import sdl2
import sdl2.ext
import ctypes
from spectrax import locals


class _EventLoop:
    """
    A class representing the event loop for handling mouse and keyboard events.

    Attributes:
        _mouse: An internal class for handling mouse events.
        _keyboard: An internal class for handling keyboard events.
        double_tap_tick (int): Number of frames to detect a double-tap event.
        double_tap_tick_at (int): Counter to track the double-tap event.
        double_tap_first_tap (bool): Flag to indicate the first tap in a potential double-tap.

    Methods:
        update(): Update the mouse and keyboard events.
    """

    class _Mouse:
        """
        An internal class representing mouse events.

        Attributes:
            pos (list): Current position of the mouse [x, y].
            posX (int): Current x-coordinate of the mouse.
            posY (int): Current y-coordinate of the mouse.
            relX (int): Relative x-coordinate change of the mouse.
            relY (int): Relative y-coordinate change of the mouse.
            rel (list): Relative mouse movement [relX, relY].
            direction (int): Direction of mouse movement (0 for horizontal, 1 for vertical).
            double_tap (bool): Flag indicating a double-tap event.
            press (bool): Flag indicating a mouse press event.
            tap (bool): Flag indicating a mouse tap event (mousedown).
            release (bool): Flag indicating a mouse release event (mouseup).
            back (bool): Flag indicating a mouse back event (used for navigation).

        Methods:
            None
        """

        def __init__(self):
            self.pos = [0, 0]
            self.posX = 0
            self.posY = 0
            self.relX = 0
            self.relY = 0
            self.rel = [0, 0]

            self.direction = None

            self.double_tap = False
            self.press = False
            self.tap = False
            self.release = False

            self.back = True

    class _Keyboard:
        """
        An internal class representing keyboard events.

        Attributes:
            key (str): The key pressed on the keyboard.
            delete (bool): Flag indicating a delete (backspace) event.

        Methods:
            None
        """

        def __init__(self):
            self.key = ""
            self.delete = False

    def __init__(self):
        """
        Initialize the EventLoop object.
        """
        self.mouse = self._Mouse()
        self.keyboard = self._Keyboard()
        self.double_tap_tick = 10
        self.double_tap_tick_at = 0
        self.double_tap_first_tap = False

    def update(self):
        """
        Update the mouse and keyboard events.
        """
        self.mouse.press = sdl2.mouse.SDL_GetMouseState(None, None) & sdl2.mouse.SDL_BUTTON(sdl2.mouse.SDL_BUTTON_LEFT)
        x, y = ctypes.c_int(0), ctypes.c_int(0)  # Create two ctypes values
        buttonstate = sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
        self.mouse.posX, self.mouse.posY = x.value, y.value
        rx, ry = ctypes.c_int(0), ctypes.c_int(0)  # Create two ctypes values
        buttonstate = sdl2.mouse.SDL_GetRelativeMouseState(ctypes.byref(rx), ctypes.byref(ry))
        self.mouse.relX, self.mouse.relY = rx.value, ry.value
        self.mouse.pos = [self.mouse.posX, self.mouse.posY]
        self.mouse.rel = [self.mouse.relX, self.mouse.relY]
        self.mouse.tap = False
        self.mouse.release = False
        self.keyboard.delete = False
        self.keyboard.key = ""
        self.mouse.back = False
        self.mouse.double_tap = False
        self.mouse.direction = None

        if self.mouse.relX > self.mouse.relY:
            self.mouse.direction = 0
        elif self.mouse.relY > self.mouse.relX:
            self.mouse.direction = 1

        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                self.mouse.tap = True
            if event.type == sdl2.SDL_MOUSEBUTTONUP:
                self.mouse.release = True
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_BACKSPACE:
                    self.keyboard.delete = True
                else:
                    if event.key.keysym.sym < 128:  # Regular ASCII characters
                        self.keyboard.key = chr(event.key.keysym.sym)
                    else:
                        self.keyboard.key = ""

        if self.double_tap_first_tap:
            self.double_tap_tick_at += 1
            if self.double_tap_tick_at > self.double_tap_tick:
                self.double_tap_first_tap = False
                self.double_tap_tick_at = 0
            else:
                if self.mouse.tap:
                    self.mouse.double_tap = True

        if self.mouse.tap:
            self.double_tap_first_tap = True


class _EventLoopInterface:
    """
    A class representing the interface to the EventLoop class.

    Attributes:
        mouse (_EventLoop._Mouse): An internal instance of _EventLoop._Mouse.
        keyboard (_EventLoop._Keyboard): An internal instance of _EventLoop._Keyboard.

    Methods:
        None
    """

    def __init__(self, event):
        self.mouse = event.mouse
        self.keyboard = event.keyboard


class Window:
    """
    A class representing a window for rendering graphics.

    Attributes:
        window (sdl2.ext.Window): The SDL2 window object.
        renderer (sdl2.ext.Renderer): The SDL2 renderer object.
        _size (tuple): Size of the window [width, height].
        _eventloop (_EventLoop): The internal event loop.
        event (_EventLoopInterface): Interface to the event loop for mouse and keyboard events.

    Methods:
        to_texture(sdl2.ext.Surface): Convert a Surface to a texture.
        clear(): Clear the window for rendering.
        draw(graphics.texture.Texture): Draw a texture on the window.
        render(): Present the rendered graphics on the window.
    """

    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
    sdl2.SDL_SetHint(sdl2.SDL_HINT_RENDER_DRIVER, b"direct3d")

    def __init__(self, title, size=locals.WINDOW_SIZE):
        """
        Initialize the Window object.

        Args:
            title (str): The title of the window.
            size (tuple): Size of the window (width, height). Default is locals.WINDOW_SIZE.
        """
        win_flags = (sdl2.SDL_WINDOW_FULLSCREEN | sdl2.SDL_WINDOW_SHOWN)
        self.window = sdl2.ext.Window(title, size, flags=win_flags)
        self.renderer = sdl2.ext.Renderer(self.window, flags=sdl2.SDL_RENDERER_ACCELERATED)
        self._size = size
        self._eventloop = _EventLoop()
        self.event = _EventLoopInterface(self._eventloop)

    def to_texture(self, surface):
        """
        Convert a Surface to a texture.

        Args:
            surface (sdl2.ext.Surface): The SDL2 surface to convert.

        Returns:
            sdl2.ext.renderer.Texture: The converted texture.
        """
        return sdl2.ext.renderer.Texture(self.renderer, surface)

    def clear(self):
        """
        Clear the window for rendering.
        """
        self._eventloop.update()
        self.renderer.clear()

    def draw(self, texture):
        """
        Draw a texture on the window.

        Args:
            texture (graphics.texture.Texture): The texture to draw.
        """
        rect = texture._rect

        if texture._rendered is None:
            texture._rendered = self.to_texture(texture._texture)

        self.renderer.copy(texture._rendered, dstrect=rect.rect)

    def render(self):
        """
        Present the rendered graphics on the window.
        """
        self.renderer.present()

    @property
    def width(self):
        """
        int: The width of the window.
        """
        return self._size[0]

    @property
    def height(self):
        """
        int: The height of the window.
        """
        return self._size[1]
