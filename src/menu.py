"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import os
from utils import es_entero
from componentes import cargar_menu_componentes

def cargar_menu():
    os.system('clear')
    print("--- MENU PRINCIPAL ---")
    print("")
    print("  1 - Componentes")
    print("  2 - Equipos")
    print("  3 - Distribuidores")
    print("  4 - Despachar")
    print("  5 - Días")
    print("  6 - Info sistema")
    print("  7 - Ficheros")
    print("  0 - Salir")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: " )

    while opcion > 7:
       print("El valor introducido no pertenece al menu")
       opcion = es_entero("Selecciona una opcion: ")

    seleccionar_opcion(opcion)


def seleccionar_opcion(opcion):
    if opcion == 1:
        cargar_menu_componentes()
    elif opcion == 2:
        print("Equipos")
    else:
        print("Gracias por usar nuestro sistema")