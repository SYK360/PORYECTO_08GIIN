"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import os

import menu
from utils import es_entero, alfa_numerico


def cargar_menu_distribuidores(data):
    os.system('clear')
    print("--- MENU DISTRIBUIDORES ---")
    print("")
    print("  1 - Alta")
    print("  2 - Modificación")
    print("  0 - Menu principal")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: " )

    while opcion > 2:
         print("El valor introducido no pertenece al menu")
         opcion = es_entero("Selecciona una opcion: ")

    seleccionar_opcion(opcion, data)

def seleccionar_opcion(opcion, data):
    if opcion == 1:
        alta_distribuidores(data)
    elif opcion == 2:
        modificacion_distribuidores(data)
    else:
        cargar_menu_principal(data)

def alta_distribuidores(data):
    os.system('clear')
    print("----------------")
    print("")
    print("Alta distribuidores")

    ref = alfa_numerico("Nombre Identificador (único): ")

    if ref in data['distribuidores']:
        os.system('clear')
        print("El distribuidor ya existe")
        cargar_menu_distribuidores(data)

    tiempo = es_entero("Tiempo de entrega: ")
    while tiempo <= 0:
        print("El valor debe ser mayor que 0")
        tiempo = es_entero("Tiempo de entrega: ")

    direccion = alfa_numerico("Dirección: ")

    data['distribuidores'][ref] = {
        'tiempo': tiempo,
        'direccion': direccion
    }

    print("Distribuidor creado correctamente")
    print("")
    print(data['distribuidores'])
    print("")
    print("Deseas introducir otro distribuidor? 1 : SI  0 : NO")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 1:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        alta_distribuidores(data)
    else:
        cargar_menu_principal(data)



def modificacion_distribuidores(data):
    print("Modificación distribuidores")


def cargar_menu_principal(data):
    menu.cargar_menu(data)