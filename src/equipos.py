"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import os
import menu

from utils import es_entero, alfa_numerico, es_float

def cargar_menu_equipos(data):
    os.system('clear')
    print("--- MENU EQUIPOS ---")
    print("")
    print("  1 - Alta")
    print("  2 - Modificación")
    print("  0 - Salir")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 2:
       print("El valor introducido no pertenece al menu")
       opcion = es_entero("Selecciona una opcion: ")

    seleccionar_opcion(opcion, data)

def seleccionar_opcion(opcion, data):
    if opcion == 1:
        alta_equipos(data)
    elif opcion == 2:
        modificacion_equipos(data)
    else:
        menu.cargar_menu(data)

def alta_equipos (data):
    os.system('clear')
    print("----------------")
    print("")
    print("Alta equipos")
    ref = alfa_numerico("Identificador (único): ")
    validar_ref(ref,data)


def agregar_componentes(data):
    print("----------------")
    print("")
    print("Agregar fuente")
    ref_fuente = alfa_numerico("Identificador fuente (único): ")
    ref_pb = alfa_numerico("Identificador placa base (único): ")
    ref_tg = alfa_numerico("Identificador tg (único): ")
    ref_cpu = alfa_numerico("Identificador cpu (único): ")
    ref_ram = alfa_numerico("Identificador ram (único): ")
    ref_disco = alfa_numerico("Identificador disco (único): ")

def agegar_fuente(data):
    print("----------------")
    print("")
    print("Agregar fuente")
    print("1 - Ingresar una referencia")
    print("2 - Listar fuentes")
    print("0 - Salir")

    opcion = es_entero("Selecciona una opcion: ")
    while opcion > 2:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
      ref_fuente = alfa_numerico("Identificador fuente (único): ")
      return ref_fuente
    elif opcion == 2:
        print("Listar fuentes")
    else:
        cargar_menu_equipos(data)



def validar_ref(ref, data):
    if ref in data['equipos']:
        os.system('clear')
        print("La referencia ya existe")
        cargar_menu_equipos(data)

def modificacion_equipos(data):
    print("Modificacion equipos")
