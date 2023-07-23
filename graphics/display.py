import sdl2
import sdl2.ext
import ctypes

from graphics import locals



class _eventloop:
    class _mouse:
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

    class _keyboard:
        def __init__(self):
            self.key = ""
            self.delete = False

    def __init__(self):
        self.mouse = self._mouse()
        self.keyboard = self._keyboard()
        self.double_tap_tick = 10
        self.double_tap_tick_at = 0
        self.double_tap_first_tap = False

    def update(self):
        self.mouse.press = sdl2.mouse.SDL_GetMouseState(None, None) & sdl2.mouse.SDL_BUTTON(sdl2.mouse.SDL_BUTTON_LEFT)
        x, y = ctypes.c_int(0), ctypes.c_int(0) # Create two ctypes values
        buttonstate = sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
        self.mouse.posX, self.mouse.posY = x.value,y.value
        rx, ry = ctypes.c_int(0), ctypes.c_int(0) # Create two ctypes values
        buttonstate = sdl2.mouse.SDL_GetRelativeMouseState(ctypes.byref(rx), ctypes.byref(ry))
        self.mouse.relX, self.mouse.relY = rx.value,ry.value
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
            

class _eventloop_interface:
    def __init__(self,event):
        self.mouse=event.mouse
        self.keyboard=event.keyboard
        
        
class Window:
    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
    sdl2.SDL_SetHint(sdl2.SDL_HINT_RENDER_DRIVER, b"direct3d")
    def __init__(self,title,size=locals.WINDOW_SIZE):
        win_flags = (sdl2.SDL_WINDOW_FULLSCREEN | sdl2.SDL_WINDOW_SHOWN)
        self.window = sdl2.ext.Window(title, size, flags=win_flags)
        self.renderer=sdl2.ext.Renderer(self.window,flags=sdl2.SDL_RENDERER_ACCELERATED)
        self._size=size
        self._eventloop=_eventloop()
        self.event=_eventloop_interface(self._eventloop)
        
    def to_texture(self,surface):
        return sdl2.ext.renderer.Texture(self.renderer,surface)
        
    def clear(self):
        self._eventloop.update()
        self.renderer.clear()
      
    def draw(self,texture):
        rect=texture._rect
        
        if texture._rendered is None:
            texture._rendered=self.to_texture(texture._texture)
         
        self.renderer.copy(texture._rendered,dstrect=rect.rect)  
        
    def render(self):
        self.renderer.present()
        
    @property
    def width(self):
        return self._size[0]
        
    @property
    def height(self):
        return self._size[1]
        
        