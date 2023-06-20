"""
@author: CARLOS ANDRES YANEZ CORREA
"""


import sys
import os

# Seteamos el path para nuestros archivos independientes.
sys.path.append('./src')

from menu import cargar_menu

data = {
    "componentes": {},
    "equipos": {},
    "distribuidores": {},
    "despachar": {},
    "dias": {},
}

os.system('clear')
cargar_menu(data)