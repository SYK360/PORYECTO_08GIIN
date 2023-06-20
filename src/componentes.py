"""
@author: CARLOS ANDRES YANEZ CORREA
"""


import os
from utils import es_entero, alfa_numerico, es_float

def cargar_menu_componentes(data):
    os.system('clear')
    print("--- MENU COMPONENTES ---")
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

    seleccionar_opcion(opcion)

def seleccionar_opcion(opcion):
    if opcion == 1:
        alta_componentes()
    elif opcion == 2:
        modificacion_componentes()
    else:
        print("Gracias por usar nuestro sistema")

def alta_componentes():
    os.system('clear')
    print("----------------")
    print("")
    print("Alta Componentes")
    ref = alfa_numerico("Identificador: ")
    tipo = seleccionar_tipo_componente()
    peso = es_entero("Peso: ")
    coste = es_float("Coste: ")
    cantidad = es_entero("Cantidad: ")

    print("Referencia: " + ref)
    print("Tipo: " + str(tipo))
    print("Peso: " + str(peso))
    print("Coste: " + str(coste))
    print("Cantidad: " + str(cantidad))


def validar_referencia(ref):
    print("Validar Referencia")

def seleccionar_tipo_componente():
    print("1 - Fuente, 2 - PB, 3 - TG, 4 - CPU, 5 - RAM, 6 - Disco")
    tipo = es_entero("Selecciona una opcion: ")
    while tipo > 6:
        print("El valor introducido no pertenece al menu")
        tipo = es_entero("Selecciona una opcion: ")

    return tipo
def modificacion_componentes():
    print("Modificación Componentes")

