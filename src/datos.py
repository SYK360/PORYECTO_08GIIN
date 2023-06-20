"""
@author: CARLOS ANDRES YANEZ CORREA
"""

from archivo import cargar_archivo, guardar_archivo

def cargar_datos(nombre_archivo):
    return cargar_archivo(nombre_archivo)

def guardar_datos(nombre_archivo, dic):
    if len(dic) == 0:
        return dic
    return guardar_archivo(nombre_archivo, dic)
