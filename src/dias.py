"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import menu
from utils import  limpiar_pantalla, es_entero
from datetime import datetime

# Funcion que carga el menu principal del apartado dias.
def cargar_menu_dias (data):
    limpiar_pantalla()
    print("--- MENU DIAS ---")
    print("")
    print("  1 - Crear")
    print("  0 - Salir")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 1:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 0:
        menu.cargar_menu(data)

    crear_dia(data)


# Esta funcion simula el paso del tiempo de un despacho.
# Se solicita al usuario el identificador del despacho y los dias que se quieren ingresar.
# Se comprueba que el despacho exista y que los dias a ingresar no superen los dias restantes.
# Se actualiza el valor de los dias restantes y se crea un registro en el diccionario dias.

def crear_dia (data) :
    despacho_ref = es_entero("Identificador despacho: ")

    if despacho_ref not in data['despachar']:
        print("El despacho no existe")
        print("")
        cargar_menu_dias(data)


    if data['despachar'][despacho_ref]['dias_restantes'] == 0:
        print("El equipo ya fue entregado !")
        print("")
        cargar_menu_dias(data)

    dias = es_entero("Dias a ingresar: ")

    if dias > data['despachar'][despacho_ref]['dias_restantes']:
        print("No se puede ingresar una cantidad superior a los dias restantes")
        print("")
        cargar_menu_dias(data)

    data['despachar'][despacho_ref]['dias_restantes']  -= dias

    clave = int(max(data['dias']) if data['dias'] else 0)
    clave += 1
    fecha = datetime.now()

    data['dias'][clave] = {
        "despacho_ref" : despacho_ref,
        "dias" : dias,
        "fecha" : fecha.strftime('%Y-%m-%d %H:%M:%S'),
        "dias_restantes_disponibles" : data['despachar'][despacho_ref]['dias_restantes']
    }

    cargar_menu_dias(data)

