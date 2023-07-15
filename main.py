"""
@author: CARLOS ANDRES YANEZ CORREA
"""


import sys

# Seteamos el path para nuestros archivos independientes.
sys.path.append('./src')

from utils import limpiar_pantalla
from menu import cargar_menu

data = {
    "componentes": {},
    "equipos": {},
    "distribuidores": {},
    "despachar": {},
    "dias": {},
}

limpiar_pantalla()
cargar_menu(data)