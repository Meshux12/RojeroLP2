# Programa principal

import datetime as d
import contacto as c
import agenda as a


c1 = c.Contacto("Maria", "1111111115", d.datetime(2000,1,30))
c2 = c.Contacto("Pepe",  "1111111119", d.datetime(2000,10,24))
c3 = c.Contacto("Ana",   "1111111117", d.datetime(2000,2,20))

a = a.Agenda()
a.agregar(c1)
a.agregar(c2)
a.agregar(c3)
print("Listar")
a.listar()
print ("Consultar: ", a.consultar("1111111119"))
print ("Borrar: ", a.borrar("1111111119"))
print("Listar")
a.listar()
print ("Modificar: ", a.modificar("1111111117", c.Contacto("Ramon","1111111115", d.datetime(2000,1,29))))
print("Listar")
a.listar()


