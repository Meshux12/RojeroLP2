#clases abstractas

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def comer(self)->None:
        pass

    def saltar(self)->None:
        print("El animal salta.")

class Perro(Animal):
    def comer(self)->None:
        print("El perro esta comiendo")

class Vaca(Animal):
    def comer(self)->None:
        print("La vaca come pastura")

v1 = Vaca()
v1.saltar()
v1.comer()