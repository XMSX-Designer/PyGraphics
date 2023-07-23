# Import necessary libraries
import sdl2
import sdl2.ext
import spectrax.superclass
import spectrax.rect
import pygame as _p
import PIL as _pil
import numpy as _np

# Helper function to convert a Pygame surface to an SDL2 surface
def _from_pgsurface(surface):
    data = _p.image.tostring(surface, "RGBA", False)
    pil_image = _pil.Image.frombuffer("RGBA", surface.get_size(), data)
    return sdl2.ext.image.pillow_to_surface(pil_image)

# Helper function to convert a NumPy array to an SDL2 surface
def _from_array(array):
    return sdl2.ext.image.pillow_to_surface(_pil.Image.fromarray(array))

# Class "Texture" to represent different types of textures
class Texture(spectrax.superclass.MultipleConstructors):

    # Constructor 1: Initialize an empty texture with the given size
    def __init1__(self, size):
        pass

    # Constructor 2: Initialize an empty texture with the given size and flags
    def __init2__(self, size, flags):
        pass

    # Constructor 3: Load a texture from a file and create a corresponding rectangle object
    def __init3__(self, filename):
        self._texture = sdl2.ext.image.load_img(filename)
        self._rect = spectrax.rect.Rect(0, 0, self._texture.w, self._texture.h)

    # Constructor 4: Load a texture from a file with custom flags (not implemented)
    def __init4__(self, filename, flags):
        pass

    # Constructor 5: Initialize a texture from an SDL2 surface and create a corresponding rectangle object
    def __init5__(self, surface):
        if not isinstance(surface, sdl2.SDL_Surface):
            raise TypeError(f"Argument 'surface' should be of type 'SDL_Surface', "
                            f"but received type '{type(surface).__name__}'.")
        self._texture = surface
        self._rect = spectrax.rect.Rect(0, 0, self._texture.w, self._texture.h)

    # Constructor 6: Initialize a texture from a Pygame surface and create a corresponding rectangle object
    def __init6__(self, pgsurface):
        if not isinstance(pgsurface, _p.Surface):
            raise TypeError(f"Argument 'pgsurface' should be of type 'pygame.Surface', "
                            f"but received type '{type(pgsurface).__name__}'.")
        self._texture = _from_pgsurface(pgsurface)
        self._rect = spectrax.rect.Rect(0, 0, self._texture.w, self._texture.h)

    # Constructor 7: Initialize a texture from a NumPy array and create a corresponding rectangle object
    def __init7__(self, array):
        if not isinstance(array, _np.ndarray):
            raise TypeError(f"Argument 'array' should be of type 'numpy.array', "
                            f"but received type '{type(array).__name__}'.")
        self._texture = _from_array(array)
        self._rect = spectrax.rect.Rect(0, 0, self._texture.w, self._texture.h)

    # Constructor 8: Initialize a texture from a PIL image and create a corresponding rectangle object
    def __init8__(self, pilimage):
        if not isinstance(pilimage, _pil.Image.Image):
            raise TypeError(f"Argument 'pilimage' should be of type 'PIL.Image.Image', "
                            f"but received type '{type(pilimage).__name__}'.")
        self._texture = sdl2.ext.image.pillow_to_surface(pilimage)
        self._rect = spectrax.rect.Rect(0, 0, self._texture.w, self._texture.h)

    # List of constructor signatures and their corresponding initializer methods
    __constructors__ = [
        (
            ("size"),
            ("size", "flags"),
            ("filename"),
            ("filename", "flags"),
            ("surface"),
            ("pgsurface"),
            ("array"),
            ("pilimage")
        ),
        (
            __init1__,
            __init2__,
            __init3__,
            __init4__,
            __init5__,
            __init6__,
            __init7__,
            __init8__
        )
    ]

    # Main constructor that handles multiple ways to initialize a texture
    def __init__(self, **kwargs):
        self._texture = None
        self._rect = None
        self._rendered = None
        self.__handle__(**kwargs)

    # Method to resize the texture
    def resize(self, scale=None, scale_to_width=None, scale_to_height=None, size=None):
        self._rect.resize(scale=scale, scale_to_width=scale_to_width, scale_to_height=scale_to_height, set_size=size)

    # Property method to get the width of the texture
    @property
    def width(self):
        return self._rect.w

    # Property method to set the width of the texture
    @width.setter
    def width(self, value):
        self._rect.w = value

    # Property method to get the height of the texture
    @property
    def height(self):
        return self._rect.h

    # Property method to set the height of the texture
    @height.setter
    def height(self, value):
        self._rect.h = value

    # Property method to get the size (width, height) of the texture
    @property
    def size(self):
        return self._rect.w, self._rect.h

    # Property method to set the size (width, height) of the texture
    @size.setter
    def size(self, value):
        self._rect.w, self._rect.h = value

    # Property method to get the position (x, y) of the texture
    @property
    def position(self):
        return self._rect.x, self._rect.y

    # Property method to set the position (x, y) of the texture
    @position.setter
    def position(self, value):
        self._rect.x, self._rect.y = value

    # Property method to get the x-coordinate of the texture position
    @property
    def xposition(self):
        return self._rect.x

    # Property method to set the x-coordinate of the texture position
    @xposition.setter
    def xposition(self, value):
        self._rect.x = value

    # Property method to get the y-coordinate of the texture position
    @property
    def yposition(self):
        return self._rect.y

    # Property method to set the y-coordinate of the texture position
    @yposition.setter
    def yposition(self, value):
        self._rect.y = value
