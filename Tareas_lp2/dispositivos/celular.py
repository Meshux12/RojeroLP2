from dispositivo_electronico import DispositivoElectronico


class Celular(DispositivoElectronico):
    def __init__(self, marca: str, precio: float):
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        super().__init__(marca)
        self.__precio = float(precio)


    def precio(self) -> float:
        return self.__precio

    def on(self) -> str:
        return f"El celular {self.marca} está encendido."

    def off(self) -> str:
        return f"El celular {self.marca} está apagado."

    def llamar(self) -> str:
        return f"El celular {self.marca} está realizando una llamada."

    def __str__(self) -> str:
        return f"Celular {self.marca} con precio ${self.__precio}"
