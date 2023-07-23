


class Rect:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    @property
    def rect(self):
        return [self.x,self.y,self.w,self.h]
    
    def resize(self, scale=None, scale_to_width=None, scale_to_height=None, set_size=None):
        w, h = self.w,self.h
        size=(w,h)
        if scale is not None:
            size= [round(w * scale), round(h * scale)]
        elif scale_to_width is not None:
            scale_factor = scale_to_width / w
            new_h = h * scale_factor
            size= [round(scale_to_width), round(new_h)]
        elif scale_to_height is not None:
            scale_factor = scale_to_height / h
            new_w = w * scale_factor
            size= [round(new_w), round(scale_to_height)]
        elif set_size is not None:
            nw, nh = set_size
            size= [round(nw), round(nh)]
        self.w,self.h=size