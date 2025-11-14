import contacto as c

class Agenda:
    def __init__(self):
        self.__contactos = []

    def agregar(self, cont: c.Contacto)->None:
        # Por simplicidad no validamos el contacto
        self.__contactos.append(cont)

    def consultar(self, cel:str)->c.Contacto:
        # Por simplicidad no validamos el celular
        for cont in self.__contactos:
            if cont.celular == cel:
                return cont
        return None
    
    def borrar(self, cel:str)->bool:
        # Por simplicidad no validamos el celular
        for cont in self.__contactos:
            if cont.celular == cel:
                self.__contactos.remove(cont)
                return True
        return False
    
    def modificar(self, cel:str, cont:c.Contacto)->bool:
        # Por simplicidad no validamos el celular y el contacto
        for i in range(len(self.__contactos)):
            if self.__contactos[i].celular == cel:
                self.__contactos[i]=cont
                return True
        return False
    
    def listar(self)->None:
        for c in self.__contactos:
            print(c)
    