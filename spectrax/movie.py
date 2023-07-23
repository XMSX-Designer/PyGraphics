import sdl2
import sdl2.ext
import cv2 as _cv2
import numpy as _np
import requests as _req

import spectrax.locals
import spectrax.texture
import spectrax.superclass


class Movie(spectrax.superclass.MultipleConstructors):
    """
    A class representing a movie player.

    Attributes:
        _mode (str): The mode of the movie player, either "file" or "url".
        _definition: The definition of the movie player.
        _audio_active: A flag indicating if the audio is active for the movie player.
        _fps: Frames per second for the movie player.
        _capture: The OpenCV VideoCapture object for file-based movies.
        _webget (function): A function to retrieve frames from a URL-based movie.
        _window: The SDL2 window object for rendering the movie frames.
        _last: The last rendered frame as a Texture.

    Methods:
        __init1__(window, path, definition, audio): Constructor for file-based movies.
        __init2__(window, url, definition, audio): Constructor for URL-based movies.
        read(): Read the next frame from the movie and render it as a Texture.
    """

    def __init1__(self, window, path, definition, audio):
        """
        Constructor for file-based movies.

        Args:
            window: The SDL2 window object.
            path (str): The path to the movie file.
            definition: The definition of the movie player.
            audio (bool): A flag indicating if audio is active for the movie player.
        """
        self._mode = "file"
        self._definition = definition
        self._audio_active = audio
        self._fps = 30
        self._capture = _cv2.VideoCapture(path)
        self._window = window
        self._last = None

    def __init2__(self, window, url, definition, audio):
        """
        Constructor for URL-based movies.

        Args:
            window: The SDL2 window object.
            url (str): The URL to retrieve the movie frames.
            definition: The definition of the movie player.
            audio (bool): A flag indicating if audio is active for the movie player.
        """

        def get():
            bytesdata = _req.get(url).content
            return _np.frombuffer(bytesdata, dtype=_np.uint8)

        self._mode = "url"
        self._definition = definition
        self._audio_active = audio
        self._fps = 30
        self._webget = get
        self._window = window
        self._last = None

    __constructors__ = [
        (
            ("window", "path", "definition", "audio"),
            ("window", "url", "definition", "audio")
        ),
        (
            __init1__,
            __init2__
        )
    ]

    def __init__(self, **kwargs):
        """
        Initialize the Movie object using one of the specified constructors.

        Args:
            **kwargs: Keyword arguments to pass to the constructors.
        """
        self._frames = None
        self._fps = None
        self._audio_active = None
        self._definition = None
        self.__handle__(**kwargs)

    def read(self):
        """
        Read the next frame from the movie and render it as a Texture.

        Returns:
            graphics.texture.Texture: A Texture object containing the rendered frame.
        """
        if self._mode == "file":
            _, frame = self._capture.read()
            if not _:
                return self._last
            elif self._last is not None:
                self._last._rendered.destroy()
            texture = spectrax.texture.Texture(array=frame)
            texture._rendered = self._window.to_texture(texture._texture)
            sdl2.SDL_FreeSurface(texture._texture)
            self._last = texture
            return texture
        elif self._mode == "url":
            frame = self._webget()
            if self._last is not None:
                self._last._rendered.destroy()
            texture = spectrax.texture.Texture(array=frame)
            texture._rendered = self._window.to_texture(texture._texture)
            sdl2.SDL_FreeSurface(texture._texture)
            self._last = texture
            return texture
