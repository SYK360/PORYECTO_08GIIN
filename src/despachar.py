"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import os
import menu
from utils import alfa_numerico, limpiar_pantalla, es_entero
from datetime import datetime


def crear_despacho (data):
    distribuidor_ref = alfa_numerico("Identificador distribuidor (único): ")

    if distribuidor_ref not in data['distribuidores']:
        print("El distribuidor no existe! ")
        print("")
        cargar_menu_despachar(data)

    equipo_ref = alfa_numerico("Identificador equipo (único): ")

    if equipo_ref not in data['equipos']:
        print("El equipo no existe! ")
        print("")
        cargar_menu_despachar(data)

    if data['equipos'][equipo_ref]['cantidad'] <= 0:
        print("El equipo no tiene cantidad disponible para su despacho")
        print("")
        cargar_menu_despachar(data)

    data['equipos'][equipo_ref]['cantidad'] -= 1

    clave = int(max(data['despechar']) if data['despachar'] else 0)
    clave += 1
    fecha = datetime.now()

    data['despachar'][clave] = {
        "distribuidor_ref": distribuidor_ref,
        "equipo_ref": equipo_ref,
        "fecha": fecha.strftime('%Y-%m-%d %H:%M:%S'),
        "dias_restantes": data['distribuidores'][distribuidor_ref]['tiempo']
    }

    print("Despacho creado correctamente")
    cargar_menu_despachar(data)


def cargar_menu_despachar (data):
    limpiar_pantalla()
    print("--- MENU DESPACHAR ---")
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

    crear_despacho(data)

