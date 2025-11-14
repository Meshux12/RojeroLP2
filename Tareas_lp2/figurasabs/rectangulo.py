from giguras import Figura

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float, color: str = "Rojo"):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def get_area(self) -> float:
        return self.base * self.altura

    def get_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def dibujar(self) -> None:
        print(f"Dibujando un rectángulo de {self.base}x{self.altura} en color {self.color}")
