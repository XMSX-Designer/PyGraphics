import sdl2
import sdl2.ext
import graphics.texture
import graphics.locals

import pygame as _p
import PIL as _pil
import PIL.ImageFont as _pil_if
import PIL.ImageDraw as _pil_id
import PIL.Image as _pil_i
import ctypes as _ct
_p.font.init()



class Font:
    """
    A class representing fonts used for rendering text.

    Attributes:
        backend (str): The graphics backend used for font rendering.
        _font (pygame.font.Font or PIL.ImageFont): The font object.

    Methods:
        render: Render the text using the selected font and backend.
    """
    def __init__(self, px, font=None, back_end=graphics.locals.backends.PYGAME):
        """
        Initialize the Font object with the specified font size and backend.

        Args:
            px (int): The font size in pixels.
            font (str): The path to the font file. If None, use the default system font.
            back_end (str): The graphics backend used for font rendering. Must be "pygame" or "pil".
        """
        self.backend = back_end
        if back_end == graphics.locals.backends.PYGAME:
            if font is None:
                self._font = _p.font.SysFont(None, px)
            else:
                self._font = _p.font.Font(font, px)

        elif back_end == graphics.locals.backends.PIL:
            self.px = px
            font = "graphics/resources/default.ttf" if font is None else font
            self._font = _pil_if.truetype(font, px)

    def render(self, *args, **kwargs):
        """
        Render the text using the selected font and backend.

        Args:
            *args: Positional arguments depending on the backend used:
                    - For Pygame backend: text (str), color (tuple), alpha (int).
                    - For PIL backend: text (str), size (tuple), color (tuple), background_color (tuple).
            **kwargs: Keyword arguments (not used in the current implementation).

        Returns:
            graphics.texture.Texture: A Texture object containing the rendered text.
        """
        if self.backend == graphics.locals.backends.PYGAME:
            text, color, alpha = args
            surface = self._font.render(str(text), alpha, color)
            texture = graphics.texture.Texture(pgsurface=surface)
            return texture

        elif self.backend == graphics.locals.backends.PIL:
            text, size, color, background_color = args
            text = str(text)
            width, height = size
            image = _pil_i.new("RGBA", (width, height), background_color)

            draw = _pil_id.Draw(image)
            text_width, text_height = draw.textsize(text, self._font)
            x = (width - text_width) // 2
            y = (height - text_height) // 2

            draw.text((x, y), text, fill=color, font=self._font)

            texture = graphics.texture.Texture(pilimage=image)
            return texture
