"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import json
import os
from utils import es_entero

def cargar_menu_sistema(data):
    os.system('clear')
    print("--- MENU SISTEMA ---")
    print("")
    print("  1 - Distribuidores")
    print("  0 - Salir")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: " )

    while opcion > 1:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        cargar_listado_distribuidores(data)


def cargar_listado_distribuidores(data):

    for clave, valor in data['distribuidores'].items():
        print(f"Nombre: {clave}, Direccion: {data['distribuidores'][clave]['direccion']}, Tiempo: {data['distribuidores'][clave]['tiempo']}")