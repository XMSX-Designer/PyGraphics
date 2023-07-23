


class MultipleConstructors:
    __constructors__=[[],[]]
    
    def __handle__(self,**kwargs):
        constructor=tuple(kwargs.keys())
        constructor=constructor[0] if len(constructor)==1 else constructor
        for i,constructor_scheme in enumerate(self.__constructors__[0]):
            if constructor==constructor_scheme:
                data=list(kwargs.values())
                self.__constructors__[1][i](self,*data)
                return i
                
        raise KeyError(f"\n    No matching constructor for initialization of {constructor}" / "Candidate constructor not viable")
        
        
        
        
        
        
        
        
        
        

        

            
            
        

    