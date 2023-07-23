import sdl2
import sdl2.ext


import cv2 as _cv2
import numpy as _np
import requests as _req

import graphics.locals
import graphics.texture
import graphics.superclass





class Movie(graphics.superclass.MultipleConstructors):
    def __init1__(self,window,path,definition,audio):
        
        self._mode="file"
        self._definition=definition
        self._audio_active=audio
        self._fps=30
        self._capture=_cv2.VideoCapture(path)
        self._window=window
        self._last=None
    
    def __init2__(self,url,path,definition,audio):
        
        
        def get():
            bytesdata=_req.get(url).content
            return _np.frombuffer(bytesdata,dtype=_np.uint8)
            
        self._mode="url"
        self._definition=definition
        self._audio_active=audio
        self._fps=30
        self._webget=get
        self._window=window
        self._last=None
                
    __constructors__=[
        (
            ("window","path","definition","audio"),
            ("window","url","definition","audio")
        ),
        (
            __init1__,
        )
    ]
        
        
        
    def __init__(self,**kwargs):
        
        self._frames=None
        self._fps=None
        self._audio_active=None
        self._definition=None
        self.__handle__(**kwargs)
    
    
    
    def read(self):
        if self._mode=="file":
            _,frame=self._capture.read()
            if not _:
                return self._last
            elif self._last is not None:
                self._last._rendered.destroy()
            texture = graphics.texture.Texture(array=frame)
            texture._rendered=self._window.to_texture(texture._texture)
            sdl2.SDL_FreeSurface(texture._texture)
            self._last=texture
            return texture
            
        elif self._mode=="url":
            frame=self._webget()
            
            if self._last is not None:
                self._last._rendered.destroy()
            texture = graphics.texture.Texture(array=frame)
            texture._rendered=self._window.to_texture(texture._texture)
            sdl2.SDL_FreeSurface(texture._texture)
            self._last=texture
            return texture    
    
    
    