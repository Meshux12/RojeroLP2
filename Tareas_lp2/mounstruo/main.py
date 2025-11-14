from monstruos import Monstruo
from monstruos import Vampiro
from monstruos import HombreLobo

def main():
    v1 = Vampiro()
    h1 = HombreLobo()

    print("\n Vampiro\n")


    v1.correr()     
    v1.atacar()     
    v1.volar()      

    print("\n Hombre Lobo\n")

    h1.correr()     
    h1.atacar()     
    h1.aullar()     

main()