from figura import Figura
import math

class Circulo(Figura):
    def __init__(self, color:str, radio:float)->None:
        super().__init__(color)
        self.radio = radio

        #Agregar propiedad de radio y su setter
    
    def get_area(self)->float:
        return math.pi * self.radio ** 2
    
    #agregar el metodo str