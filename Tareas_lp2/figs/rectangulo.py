from figu import Figura

class Rectangulo(Figura):
    def __init__(self, color: str, base: float, altura: float):
        super().__init__(color)
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

    def get_area(self) -> float:
        return self.base * self.altura

    def __str__(self) -> str:
        return f"Rectángulo {self.color}, base {self.base}, altura {self.altura}, área {self.get_area():.2f}"
