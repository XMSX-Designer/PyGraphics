import sdl2
import sdl2.ext

import graphics.superclass
import graphics.rect

import pygame as _p
import PIL as _pil
import numpy as _np

def _from_pgsurface(surface):
    data=_p.image.tostring(surface,"RGBA",False)
    pil_image=_pil.Image.frombuffer("RGBA",surface.get_size(),data)
    return sdl2.ext.image.pillow_to_surface(pil_image)
    

def _from_array(array):
    return sdl2.ext.image.pillow_to_surface(_pil.Image.fromarray(array))
        
class Texture(graphics.superclass.MultipleConstructors):
    
    def __init1__(self,size):
        pass
        
    def __init2__(self,size,flags):
        pass  
        
    def __init3__(self,filename):
        self._texture=sdl2.ext.image.load_img(filename)
        self._rect=graphics.rect.Rect(0,0,self._texture.w,self._texture.h)
        
    def __init4__(self,filename,flags):
        pass       
        
    def __init5__(self,surface):
        if not isinstance(surface,sdl2.SDL_Surface):
            raise TypeError(f"Argument 'surface' should be of type 'SDL_Surface', " \
               f"but received type '{type(surface).__name__}'.")
        self._texture=surface
        self._rect=graphics.rect.Rect(0,0,self._texture.w,self._texture.h)
        
    def __init6__(self,pgsurface):
        if not isinstance(pgsurface,_p.Surface):
            raise TypeError(f"Argument 'pgsurface' should be of type 'pygame.Surface', " \
               f"but received type '{type(pgsurface).__name__}'.")
               
        self._texture=_from_pgsurface(pgsurface)
        self._rect=graphics.rect.Rect(0,0,self._texture.w,self._texture.h)
        
    def __init7__(self,array):
        if not isinstance(array,_np.ndarray):
            raise TypeError(f"Argument 'array' should be of type 'numpy.array', " \
               f"but received type '{type(array).__name__}'.")
        self._texture=_from_array(array)
        self._rect=graphics.rect.Rect(0,0,self._texture.w,self._texture.h)
        
    def __init8__(self,pilimage):
        if not isinstance(pilimage,_pil.Image.Image):
            raise TypeError(f"Argument 'pilimage' should be of type 'PIL.Image.Image', " \
               f"but received type '{type(pilimage).__name__}'.")
        self._texture=sdl2.ext.image.pillow_to_surface(pilimage)
        self._rect=graphics.rect.Rect(0,0,self._texture.w,self._texture.h)
        
    __constructors__=[
        (
            ("size"),
            ("size","flags"),
            ("filename"),
            ("filename","flags"),
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
        
    def __init__(self,**kwargs):
        
        self._texture=None
        self._rect=None
        self._rendered=None
        
        self.__handle__(**kwargs)
    
    def resize(self,scale=None,scale_to_width=None,scale_to_height=None,size=None):
        self._rect.resize(scale=scale,scale_to_width=scale_to_width,scale_to_height=scale_to_height,set_size=size)
        
    @property
    def width(self):
        return self._rect.w
        
    @width.setter
    def width(self,value):
        self._rect.w=value
        
    @property
    def height(self):
        return self._rect.h
        
    @height.setter
    def height(self,value):
        self._rect.h=value
        
    @property
    def size(self):
        return self._rect.w,self._rect.h
        
    @size.setter
    def size(self,value):
        self._rect.w,self._rect.h=value
    
    @property
    def position(self):
        return self._rect.x,self._rect.y
        
    @position.setter
    def position(self,value):
        self._rect.x,self._rect.y=value
        
    @property
    def xposition(self):
        return self._rect.x
        
    @xposition.setter
    def xposition(self,value):
        self._rect.x=value
        
    @property
    def yposition(self):
        return self._rect.y
    
    @yposition.setter
    def yposition(self,value):
        self._rect.y=value
        
        
    
        
        