base_de_datos = {}
x = 1
z = 0

while x == 1:
    print("introduzca 1, para añadir alumno (alumno:aprobado/suspenso)\n"
          "introduzca 2, para comprobar el numero de aprobados\n"
          "introduzca 3, para mostrar toda la clase")
    y = int(input("¿Que desea?"))
    if y == 1:
        nombre = input("añadir alumno (alumno:aprobado/suspenso)\n"
                       "todo en minusculas porfavor")
        a, b = nombre.split(":")
        base_de_datos[a] = b
    elif y == 2:
        g = list(base_de_datos.values())
        t = g.count("true")       
        print("El numero de aprobados es:",t)
    elif y == 3:
        print(base_de_datos)
