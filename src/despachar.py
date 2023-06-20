"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import os
import menu
from utils import  es_entero, alfa_numerico

def cargar_menu_despachar (data):
    os.system("clear")
    print("--- MENU DESPACHAR ---")
    print("")
    distribuidor_id = alfa_numerico("Identificador distribuidor (único): ")
    equipo_id = alfa_numerico("Identificador equipo (único): ")

    print(distribuidor_id)
    print(equipo_id)

    menu.cargar_menu(data)