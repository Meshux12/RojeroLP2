from celular import Celular
from television import Television


def main():
    celular1 = Celular("Samsung", 8500.50)
    tv1 = Television("Sony", 200)

    print(celular1)
    print(celular1.on())
    print(celular1.llamar())
    print(celular1.off())
    print(f"Precio del celular: ${celular1.precio()}")

    print(tv1)
    print(tv1.on())
    print(tv1.verNetflix())
    print(tv1.off())
    print(f"Cantidad de canales: {tv1.canales()}")

main()
