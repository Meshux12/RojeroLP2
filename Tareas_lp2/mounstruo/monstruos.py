class Monstruo:
    def correr(self):
        print("El monstruo esta corriendo...")

    def atacar(self):
        print("El monstruo esta atacando ataca...")

class Vampiro(Monstruo):
    def volar(self):
        print("El vampiro empieza a volar...")

    def atacar(self):
        print("El vampiro esta atacando..")

class HombreLobo(Monstruo):
    def aullar(self):
        print("El hombre lobo empieza a aullar...")

    def correr(self):
        print("El hombre lobo viene por ti...")
