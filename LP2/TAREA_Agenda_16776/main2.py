import agenda as a
import contacto as c
import datetime as d
import random

a = a.Agenda()
while True:
    print("***** Agenda de Contactos *****")
    print("1. Agregar")
    print("2. Borrar")
    print("3. Consultar")
    print("4. Modificar")
    print("5. Listar")
    print("6. Salir")
    try:
        op = int(input("Opcion: "))

        if op == 1:  # Agregar
            nombre = input("Nombre del contacto: ")
            celular = input("Celular: ")
            anio = random.randint(1980, 2020)
            mes = random.randint(1, 12)
            dia = random.randint(1, 28)  # mejor 28 para no tener fechas inválidas
            a.agregar(c.Contacto(nombre, celular, d.datetime(anio, mes, dia)))

        elif op == 2:  # Borrar
            celular = input("Celular del contacto a borrar: ")
            if a.borrar(celular):
                print("Contacto borrado.")
            else:
                print("No se encontró el contacto.")

        elif op == 3:  # Consultar
            celular = input("Celular del contacto a consultar: ")
            cont = a.consultar(celular)
            if cont:
                print("Contacto encontrado:", cont)
            else:
                print("No se encontró el contacto.")

        elif op == 4:  # Modificar
            celular = input("Celular del contacto a modificar: ")
            nombre = input("Nuevo nombre: ")
            nuevo_cel = input("Nuevo celular: ")
            anio = int(input("Año de nacimiento: "))
            mes = int(input("Mes de nacimiento: "))
            dia = int(input("Día de nacimiento: "))
            nuevo = c.Contacto(nombre, nuevo_cel, d.datetime(anio, mes, dia))
            if a.modificar(celular, nuevo):
                print("Contacto modificado.")
            else:
                print("No se encontró el contacto.")

        elif op == 5:  # Listar
            print("** Lista de Contactos **")
            a.listar()

        elif op == 6:  # Salir
            print("Fin")
            break

        else:
            print("Opción inválida")

    except ValueError as ve:
        print("ValueError:", ve)
    except TypeError as te:
        print("TypeError:", te)
