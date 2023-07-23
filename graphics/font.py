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



def from_pgsurface(surface):
    data=_p.image.tostring(surface,"RGBA",False)
    pil_image=_pil.Image.frombuffer("RGBA",surface.get_size(),data)
    return sdl2.ext.image.pillow_to_surface(pil_image)
    

def from_array(array):
    return sdl2.ext.image.pillow_to_surface(_pil.Image.fromarray(array))

class Font:
    def __init__(self,px,font=None,back_end=graphics.locals.backends.PYGAME):
        self.backend=back_end
        if back_end==graphics.locals.backends.PYGAME:
            if font is None:
                self._font=_p.font.SysFont(None,px)
            else:
                self._font=_p.font.Font(font,px)
        
        elif back_end==graphics.locals.backends.PIL:
            self.px=px
            font="graphics/rescources/default.ttf" if font is None else font
            self._font = _pil_if.truetype(font, px)
            
    def render(self,*args,**kwargs):
        if self.backend==graphics.locals.backends.PYGAME:
            text,color,a0=args#list(kwargs.values())
            surface=self._font.render(str(text),a0,color)
            texture=graphics.texture.Texture(pgsurface=surface)
            return texture
            
        elif self.backend==graphics.locals.backends.PIL:
            text,size,color,background_color=args#,list(kwargs.values())
            text=str(text)
            width,height=size
            image = _pil_i.new("RGBA", (width, height), background_color)
            
            draw = _pil_id.Draw(image)
            text_width, text_height = draw.textsize(text, self._font)
            x = (width - text_width) // 2
            y = (height - text_height) // 2

            draw.text((0,0), text, fill=color, font=self._font)
            
            texture=graphics.texture.Texture(pilimage=image)
            return texture
        
        
        
