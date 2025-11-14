from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self, color: str):
        self.__color = color


    
    @property
    def color(self) -> str:
        return self.__color
    


    @color.setter
    def color(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError("color debe ser texto")
        self.__color = color

    @abstractmethod
    def get_area(self) -> float:
        pass


    @abstractmethod
    def get_perimetro(self) -> float:   
        pass

    @abstractmethod
    def dibujar(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Figura [{self.color}]"

    def __str__(self) -> str:
        return f"Figura de color {self.color}"
