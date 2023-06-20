"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import json
import menu

from utils import es_entero

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
       data = cargar_archivo("collection")
       cargar_menu_principal(data)
    elif opcion == 2:
        guardar_archivo("collection", data)
        cargar_menu_principal(data)
    else:
        menu.cargar_menu(data)

def cargar_archivo(nombre_archivo):
    try:
        crear_archivo(nombre_archivo)
        archivo = open(nombre_archivo,"r")
        data = json.load(archivo)
        archivo.close()
        return data
    except ValueError:
        print(ValueError)
        return {}

def crear_archivo(nombre_archivo):
    try:
        file = open(nombre_archivo,"a")
        file.close()
    except ValueError:
        print(ValueError)


def guardar_archivo(nombre_archivo, data):
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