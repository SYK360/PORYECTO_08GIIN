"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import json
from utils import es_entero

def cargar_menu_archivos(data):
    print("1 - Cargar datos")
    print("2 - Guardar datos")
    print("0 - Salir")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: " )

    while opcion > 2:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        cargar_archivo("data")
    elif opcion == 2:
        guardar_archivo("collection", data)


def cargar_archivo(nombre_archivo):
    nombre_archivo = nombre_archivo
    try:
        crear_archivo(nombre_archivo)
        archivo = open(nombre_archivo,"r")
        dic = json.load(archivo)
        archivo.close()
        return dic
    except ValueError:
        print(ValueError)
        return {}

def crear_archivo(nombre_archivo):
    nombre_archivo = nombre_archivo

    try:
        file = open(nombre_archivo,"a")
        file.close()
    except ValueError:
        print(ValueError)


def guardar_archivo(nombre_archivo, data):
    nombre_archivo = nombre_archivo

    try:
        crear_archivo(nombre_archivo)
        archivo = open(nombre_archivo,"w")
        archivo.write(json.dumps(data))
        archivo.close()
        return data
    except ValueError:
        print(ValueError)
        return {}