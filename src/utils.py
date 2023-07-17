"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import os

# Usaremos este archivo para almacenar funciones de utilidad que nos sirvan en varios modulos

# Este metodo se encarga de limpiar la pantalla dependiento el sistema operativo
def limpiar_pantalla () :
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac o Linux(os.name == 'posix')
    else:
        os.system('clear')


# Este metodo se encarga de validar que el valor ingresado sea un numero entero
# Retorna el valor ingresado por el usuario

def es_entero(str):
    es_correcto = False
    valor = 0

    while(not es_correcto):
        try:
            valor = int(input(str))
            es_correcto = True
        except ValueError:
            print("Debes introducir un numero entero")
    return valor

# Este metodo se encarga de validar que el valor ingresado sea una cadena
# Retorna el valor ingresado por el usuario
def es_str(text):
    es_correcto = False
    valor = 0

    while(not es_correcto):
        try:
            valor = str(input(text))
            es_correcto = True
        except ValueError:
            print("Debes introducir un texto")
    return valor

# Este metodo se encarga de validar que el valor ingresado sea alfanumerico
# Retorna el valor ingresado por el usuario
def alfa_numerico(text, min = 3):
    es_correcto = False
    valor = 0

    while(not es_correcto):
        try:
            valor = str(input(text))
            if len(valor) < min:
                print("El identificador debe tener al menos " + str(min) +" caracteres")
            else:
                es_correcto = True
        except ValueError:
            print("Debes introducir un texto")
    return valor

# Este metodo se encarga de validar que el valor ingresado sea un numero decimal
# Retorna el valor ingresado por el usuario
def es_float(text):
    es_correcto = False
    valor = 0

    while(not es_correcto):
        try:
            valor = float(input(text))
            es_correcto = True
        except ValueError:
            print("Debes introducir un numero decimal")
    return valor
