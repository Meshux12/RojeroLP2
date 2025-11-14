from circulo import Circulo
from rectangulo import Rectangulo

def main():
    c = Circulo(5, "Naranja")
    r = Rectangulo(4, 6, "Magenta")

    print(c)
    c.dibujar()
    print("-------------------------------------")
    print(r)
    r.dibujar()

if __name__ == "__main__":
    main()
