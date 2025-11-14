from dispositivo_electronico import DispositivoElectronico


class Television(DispositivoElectronico):
    def __init__(self, marca: str, canales: int):
        if not isinstance(canales, int):
            raise TypeError("La cantidad de canales debe ser un número entero.")
        if canales <= 0:
            raise ValueError("La televisión debe tener al menos un canal.")
        super().__init__(marca)
        self.__canales = canales

    def canales(self) -> int:
        return self.__canales

    def on(self) -> str:
        return f"La televisión {self.marca} está encendida."

    def off(self) -> str:
        return f"La televisión {self.marca} está apagada."

    def verNetflix(self) -> str:
        return f"La televisión {self.marca} está reproduciendo Netflix."

    def __str__(self) -> str:
        return f"Televisión {self.marca} con {self.__canales} canales"
