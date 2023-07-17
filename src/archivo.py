"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import json
import menu
import os

from utils import es_entero

# Renderiza el menu de archivos
# Con esto podremos guardar o cargar un archivo que ya exista
def cargar_menu_archivos(data):
    print("1 - Cargar datos")
    print("2 - Guardar datos")
    print("0 - Menu principal")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: " )

    while opcion > 2:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
       data = cargar_archivo()
       cargar_menu_principal(data)
    elif opcion == 2:
        guardar_archivo(data)
        cargar_menu_principal(data)
    else:
        menu.cargar_menu(data)

# Carga un archivo que ya existe
# si no existe, se le pedira al usuario que ingrese un nombre de archivo valido
def cargar_archivo():

    nombre_archivo = ""
    archivo_existe = False

    while (not archivo_existe):
        nombre_archivo = input("Escribe el nommbre del archivo que se desea cargar: ")
        if os.path.isfile(nombre_archivo):
            archivo_existe = True
        else:
            print("El archivo no existe !")

    try:
        crear_archivo(nombre_archivo)
        archivo = open(nombre_archivo,"r")
        data = json.load(archivo)
        archivo.close()
        return data
    except ValueError:
        print(ValueError)
        return {}

# Funcion que verifica si el archivo existe, si no existe lo crea
# Lo abre en fomo append. Esto es para que si el archivo no existe, lo cree
def crear_archivo(nombre_archivo):
    try:
        file = open(nombre_archivo,"a")
        file.close()
    except ValueError:
        print(ValueError)


# Funcion que almacena los datos en un archivo
# Si el archivo no existe, lo crea
# Si el archivo existe, lo sobreescribe
def guardar_archivo(data):

    nombre_archivo = input("Escribe el nommbre del archivo que se desea guardar: ")

    try:
        crear_archivo(nombre_archivo)
        archivo = open(nombre_archivo,"w")
        archivo.write(json.dumps(data))
        archivo.close()
        return data
    except ValueError:
        print(ValueError)
        return {}

def cargar_menu_principal(data):
    menu.cargar_menu(data)