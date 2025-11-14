from figu import Figura
import math

class Circulo(Figura):
    def __init__(self, color: str, radio: float):
        super().__init__(color)
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio

    def get_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def __str__(self) -> str:
        return f"Círculo {self.color}, radio {self.radio}, área {self.get_area():.2f}"
    

