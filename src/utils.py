
import os
def limpiar_pantalla () :
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac o Linux(os.name == 'posix')
    else:
        os.system('clear')


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
