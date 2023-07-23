


class VScroll:
    def __init__(self,upper,lower):
        self._objects = {}
        self._velocity = 0
        self._friction = 0.1
        self._y=0
        self.upper=upper
        self.lower=lower
    def addObject(self, id, obj):
        self._objects[str(id)]=obj

    def update(self, event):
        relx, rely=event.mouse.rel
        
        
        first=True
        
        new_y=0
        y=self._y
        if event.mouse.press:
                new_y += rely
                if first:
                    first=False
                    self._y+=rely
                self._velocity = rely
                
        else:
                new_y+=self._velocity
                if first:
                    first=False
                    self._y+=self._velocity
                self._velocity *= (1 - self._friction)
        """        
        if self._y>self.upper:
                self._y=self.upper
                new_y=0
                
        elif self._y<-self.lower:
                self._y=-self.lower
                new_y=0
        """        
        for id, obj in self._objects.copy().items():
            oy = obj.yposition
            new_y2=oy+new_y
            obj.yposition=new_y2

    def set_friction(self, friction):
        self._friction = friction