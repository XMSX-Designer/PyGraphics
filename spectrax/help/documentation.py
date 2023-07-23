import spectrax.font
import spectrax.display
import spectrax.locals
import spectrax.scroll


class simple:
    def __init__(self):
        self.window=spectrax.display.Window("simple doc")
        
        
        
        self.doc=open("spectrax/rescources/simple_doc.txt").read()
        
        font="spectrax/rescources/default.ttf"
        scalar=0.8
        
        self.font=spectrax.font.Font(
            round(self.window.height//100*scalar),
            font=font,
            back_end=spectrax.locals.backends.PIL)
            
        self.font_inter=spectrax.font.Font(
            round(self.window.height//80*scalar),
            font=font,
            back_end=spectrax.locals.backends.PIL)
            
        self.font_med=spectrax.font.Font(
            round(self.window.height//60*scalar),
            font=font,
            back_end=spectrax.locals.backends.PIL)
        
        self.font_large=spectrax.font.Font(
            round(self.window.height//40*scalar),
            font=font,
            back_end=spectrax.locals.backends.PIL)
        
        self.textures=[]
        self.scroll=spectrax.scroll.VScroll(0,5000)
        self.scroll.set_friction(0.05)
        y=0
        scalar=1.2
        for i,line in enumerate(self.doc.splitlines()):
            #text=self.font.render(line,[255,255,255],True)
            prefix=""#str(i)+" - "
            if i in [0,1]:
                text=self.font_large.render(prefix+line,[self.window.width,round(self.font_large.px*scalar)],(255,255,255),(0,0,0,0))
                
            elif line.startswith("##"):
                text=self.font_inter.render(prefix+line.replace("## ",""),[self.window.width,round(self.font_inter.px*scalar)],(255,255,255),(0,0,0,0))
                
            elif line.startswith("#"):
                text=self.font_med.render(prefix+line.replace("# ",""),[self.window.width,round(self.font_med.px*scalar)],(255,255,255),(0,0,0,0))
                
            else:
                text=self.font.render(prefix+line,[self.window.width,round(self.font.px*scalar)],(255,255,255),(0,0,0,0))
            text.yposition=y
            y+=round(text.height)
            self.textures.append(text)
            self.scroll.addObject(str(i),text)
            
    def exec(self):
        self.window.clear()
        self.scroll.update(self.window.event)
        
        for line in self.textures:
            self.window.draw(line)
        
        
        self.window.render()
            
