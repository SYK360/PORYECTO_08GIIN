"""
@author: CARLOS ANDRES YANEZ CORREA
"""


import sys

# Seteamos el path para nuestros archivos independientes.
sys.path.append('./src')

# Importamos las funciones que usaremos.
from utils import limpiar_pantalla
from menu import cargar_menu


# Inicicalizamos diccionarios.
data = {
    "componentes": {},
    "equipos": {},
    "distribuidores": {},
    "despachar": {},
    "dias": {},
}

# Limpiamos la pantalla y cargamos menu principal.
limpiar_pantalla()
cargar_menu(data)