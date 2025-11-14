from abc import ABC, abstractmethod

class DispositivoElectronico(ABC):
    def __init__(self, marca: str):
        if not isinstance(marca, str):
            raise TypeError("La marca debe ser una cadena de texto.")
        self._marca = marca  

    @property
    def marca(self) -> str:
        return self._marca

    @marca.setter
    def marca(self, nueva_marca: str):
        if not isinstance(nueva_marca, str):
            raise TypeError("La nueva marca debe ser una cadena de texto.")
        self._marca = nueva_marca

    @abstractmethod
    def on(self) -> str:
        pass

    @abstractmethod
    def off(self) -> str:
        pass

    def __str__(self) -> str:
        return f"Dispositivo electrónico de marca {self.marca}"
