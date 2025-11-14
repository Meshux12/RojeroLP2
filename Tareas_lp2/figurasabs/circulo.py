from giguras import Figura
import math

class Circulo(Figura):
    def __init__(self, radio: float, color: str = "Azul"):
        super().__init__(color)
        self.radio = radio

    def get_area(self) -> float:
        return math.pi * self.radio**2

    def get_perimetro(self) -> float:
        return 2 * math.pi * self.radio

    def dibujar(self) -> None:
        print(f"Dibujando un círculo de radio {self.radio} en color {self.color}")
