class Figura:
    def __init__(self, color:str)->None:
        self.color = color

    @property
    def color(self)->str:
        return self.__color
    
    @color.setter
    def color(self,color:str)->None:
        if not isinstance(color, str):
            raise TypeError("Base debe ser un str")
        self.__color = color

    def get_area(self)->float:
        return 0
    
    def __str__(self):
        return self.color