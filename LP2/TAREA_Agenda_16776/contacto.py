import datetime

class Contacto:
    def __init__(self, nombre:str, celular:str, fnac:datetime)->None:
        self.nombre = nombre
        self.celular = celular
        self.fnac = fnac
    
    @property
    def fnac(self)->datetime:
        return self.__fnac
    
    @fnac.setter
    def fnac(self, fnac:datetime)->None:
        if not isinstance(fnac, datetime.datetime):
            raise TypeError("Error. Fecha de nacimiento debe ser un datetime")
        if fnac.year <= 1900:
            raise ValueError("Error. La fecha de nacimiento debe ser mayor a 1900")
        self.__fnac = fnac

    @property
    def celular(self)->str:
        return self.__celular

    @celular.setter
    def celular(self, celular:str):
        if not isinstance(celular, str):
            raise TypeError("Error. El celular debe ser un str")
        if not celular.isnumeric() or len(celular) != 10:
            raise ValueError("Error. Celular debe tener 10 digitos")
        self.__celular = celular
        
    @property
    def nombre(self)->str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre:str)->None:
        if not isinstance(nombre, str):
            raise TypeError("Error. El nombre debe ser un str")
        self.__nombre = nombre

    def __str__(self):
        return self.nombre + "  " + self.celular
        

