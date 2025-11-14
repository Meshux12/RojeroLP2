def mostrar_todos()->None:
    print("Lista de alumnos")
    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","r")

    for alumno in f:
        print(alumno.strip())
    f.close()

def buscar_matricula(matricula:str)->None:
    print(f"Buscando alumno con matrícula {matricula}")
    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","r")
    for alumno in f:
        datos = alumno.strip().split(",")
        if datos[0] == matricula:
            print("Encontrado:", alumno.strip())
            break
    else:
        print("No se encontró el alumno.")
    f.close()

def menores_a(edad:int)->None:
    print(f"Alumnos menores a {edad}")
    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","r")
    for alumno in f:
        datos = alumno.strip().split(",")
        if int(datos[2]) < edad:
            print(alumno.strip())
    f.close()

def agregar_alumno()->None:
    matricula = input("Matrícula: ")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    sexo = input("Sexo (H/M): ")

    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","a")
    f.write(f"{matricula},{nombre},{edad},{sexo}\n")
    f.close()
    print("Alumno agregado correctamente.")

def borrar_alumno(matricula:str)->None:
    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","r")
    alumnos = f.readlines()
    f.close()

    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","w")
    borrado = False
    for alumno in alumnos:
        datos = alumno.strip().split(",")
        if datos[0] != matricula:
            f.write(alumno)
        else:
            borrado = True
    f.close()

    if borrado:
        print("Alumno borrado.")
    else:
        print("No se encontró la matrícula.")

def modificar_alumno(matricula:str)->None:
    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","r")
    alumnos = f.readlines()
    f.close()

    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","w")
    modificado = False
    for alumno in alumnos:
        datos = alumno.strip().split(",")
        if datos[0] == matricula:
            print("Alumno encontrado:", alumno.strip())
            nombre = input("Nuevo nombre: ")
            edad = input("Nueva edad: ")
            sexo = input("Nuevo sexo (H/M): ")
            f.write(f"{matricula},{nombre},{edad},{sexo}\n")
            modificado = True
        else:
            f.write(alumno)
    f.close()

    if modificado:
        print("Alumno modificado.")
    else:
        print("No se encontró la matrícula.")


def mostrar_sexo(sexo:str)->None:
    print("Alumnos por sexo")
    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","r")

    for alumno in f:
        datos = alumno.strip().split(",")
        if datos[3] == sexo:
            print(f"{datos[1]}  {datos[3]}")

def promedio_edad()->None:
    f = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","r")

    contador = 0
    suma = 0
    for alumno in f:
        datos = alumno.strip().split(",")
        suma += int(datos[2])
        contador += 1

    prom = suma / contador
    print(f"El promedio de las edades es {prom:.1f}")
    f.close()

def respaldo(arch:str)->None:
    print("Haciendo respaldo")
    f1 = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","r")
    f2 = open(f"C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt{arch}","w")

    for alumno in f1:
        f2.write(alumno)

    f1.close()
    f2.close()


def respaldo_sexo(sexo:str, arch:str)->None:
    print(f"Haciendo respaldo por sexo {sexo}")
    f1 = open("C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt","r")
    f2 = open(f"C:/Users/yoshi/OneDrive/Escritorio/LP2/TAREA_Escuela_16776/escuela.txt{arch}","w")

    for alumno in f1:
        datos = alumno.strip().split(",")
        if datos[3] == sexo:
            f2.write(alumno)

    f1.close()
    f2.close()
    print("Respaldo creado.")

# Programa principal
while True:
    print("***** Escuela *****")
    print("1. Mostrar todos los alumnos")
    print("2. Mostrar alumnos por sexo")
    print("3. Seleccionar un alumno por su matrícula")
    print("4. Seleccionar los alumnos menores a cierta edad")
    print("5. Mostrar la edad promedio de los alumnos")
    print("6. Agregar un alumno")
    print("7. Borrar un alumno")
    print("8. Modificar los datos de un alumno")
    print("9. Hacer un respaldo del archivo")
    print("10. Hacer un respaldo del archivo por sexo")
    print("11. Salir")
    try:
        op = int(input("Opción: "))

        if op == 1:
            mostrar_todos()
        elif op == 2:
            sexo = input("Mostrar alumnos por sexo (H,M): ")
            mostrar_sexo(sexo)
        elif op == 3:
            matricula = input("Matrícula a buscar: ")
            buscar_matricula(matricula)
        elif op == 4:
            edad = int(input("Edad máxima: "))
            menores_a(edad)
        elif op == 5:
            promedio_edad()
        elif op == 6:
            agregar_alumno()
        elif op == 7:
            matricula = input("Matrícula a borrar: ")
            borrar_alumno(matricula)
        elif op == 8:
            matricula = input("Matrícula a modificar: ")
            modificar_alumno(matricula)
        elif op == 10:
            sexo = input("Sexo (H,M): ")
            respaldo_sexo(sexo, f"respaldo_{sexo}.txt")
        elif op == 11:
            print("Fin")
            break
        else:
            print("Opción inválida")
    except ValueError as ve:
        print("ValueError:", ve)
    except TypeError as te:
        print("TypeError:", te)
