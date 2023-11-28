
    
nombres = ["jose miguel", "aitor menta", "benito camelas"]

def OrdenarNombre(nombre_Apellido):
    
    """Funcion: recibe un nombre y un apellido y devuelve apellido nombre
    
        - Parametros:
            - Nombre en el formato: Nombre Apellido
            
        - Salida:
            - Nombre en el formato: Apellido, Nombre"""
    x = nombre_Apellido.split(" ")
    apellido = x[-1]
    nombre = " ".join(x[:-1])

    nombre_ordenado = (apellido, nombre)
    

    print(nombre_ordenado)
    return nombre_ordenado


def ListaNombre(nombre_apellido):
    
    """Funcion: la funcion recibe una lista y la ordena por apellidos en 
                orden alfabetico
         
        - Parametros:
            - Lista de nombres: esta lista guarda una cantidad indeterminada
            de nombres:
                ["Nombre Apellido 1", ..."Nombre apellido N"]

        - Salida:
            - Devuelve una lista de nombres ordenados alfabeticamente:
            ["Apellido, Nombre 1", ... "Apellido, Nombre N"]
              """
    
    nombres.sort(key = OrdenarNombre)
    
    return nombres

ListaNombre(nombres)