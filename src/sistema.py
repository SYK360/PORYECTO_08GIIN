"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import json
import os
from utils import es_entero
import menu
import componentes
import distribuidores


def cargar_menu_sistema(data):
    os.system('clear')
    print("--- MENU SISTEMA ---")
    print("")
    print("  1 - Distribuidores")
    print("  2 - Componentes")
    print("  0 - Salir")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: " )

    while opcion > 2:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        cargar_listado_distribuidores(data)
    elif opcion == 2:
        cargar_listado_componentes(data)


def cargar_listado_componentes(data):

    for clave, valor in data['componentes'].items():
        print(f"Nombre: {clave}, Cantidad: {data['componentes'][clave]['cantidad']}, Coste: {data['componentes'][clave]['coste']}")\

    print("Deseas introducir otro componente? 1 : SI  0 : NO")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 1:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        componentes.alta_componentes(data)
    else:
        cargar_menu_principal(data)

def cargar_menu_principal(data):
    menu.cargar_menu(data)

def cargar_listado_distribuidores(data):

    for clave, valor in data['distribuidores'].items():
        print(f"Nombre: {clave}, Direccion: {data['distribuidores'][clave]['direccion']}, Tiempo: {data['distribuidores'][clave]['tiempo']}")


    print("Deseas introducir otro distribuidor? 1 : SI  0 : NO")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 1:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        distribuidores.alta_distribuidores(data)
    else:
        cargar_menu_principal(data)