from circulo import Circulo
from rectangulo import Rectangulo
from figu import Figura

def main():
    f = Figura("negro")  
    c = Circulo("verde", 5)
    r = Rectangulo("rojo", 4, 6)

    print(f)
    print(c)
    print(r)

if __name__ == "__main__":
    main()

 


