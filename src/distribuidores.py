"""
@author: CARLOS ANDRES YANEZ CORREA
"""


from utils import es_entero, alfa_numerico, limpiar_pantalla
import sistema
import menu


# Menu prinicpal de distribuidores.
def cargar_menu_distribuidores(data):
    limpiar_pantalla()
    print("--- MENU DISTRIBUIDORES ---")
    print("")
    print("  1 - Alta")
    print("  2 - Modificación")
    print("  0 - Menu principal")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: " )

    while opcion > 2:
         print("El valor introducido no pertenece al menu")
         opcion = es_entero("Selecciona una opcion: ")

    seleccionar_opcion(opcion, data)

# Funcion para manejar la seleccion del usuario.
def seleccionar_opcion(opcion, data):
    if opcion == 1:
        alta_distribuidores(data)
    elif opcion == 2:
        modificacion_distribuidores(data)
    else:
        menu.cargar_menu(data)

# Funcion para dar de alata un distribuidor.
# Se solicita el nombre, tiempo de entrega y direccion.
# En el caso de existir el nombre se informa al usuario y se vuelve a solicitar.
def alta_distribuidores(data):
    limpiar_pantalla()
    print("----------------")
    print("")
    print("Alta distribuidores")

    ref = alfa_numerico("Nombre Identificador (único): ")

    if ref in data['distribuidores']:
        limpiar_pantalla()
        print("El distribuidor ya existe")
        cargar_menu_distribuidores(data)

    tiempo = es_entero("Tiempo de entrega: ")
    while tiempo <= 0:
        print("El valor debe ser mayor que 0")
        tiempo = es_entero("Tiempo de entrega: ")

    direccion = alfa_numerico("Dirección: ")

    data['distribuidores'][ref] = {
        'tiempo': tiempo,
        'direccion': direccion
    }

    print("Distribuidor creado correctamente")
    print("")
    print("Deseas introducir otro distribuidor? 1 : SI  0 : NO")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 1:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        alta_distribuidores(data)
    else:
        menu.cargar_menu(data)

# Menu para modificacion de distribuidores.
# Se solicita el nombre del distribuidor a modificar.
# En el caso de no existir se informa al usuario y se vuelve a solicitar.
# Se solicita el campo a modificar.
def modificar_distribuidor (data):
    limpiar_pantalla()
    print("----------------")
    ref = alfa_numerico("Identificador (único): ")
    if ref not in data['distribuidores']:
        limpiar_pantalla()
        print("El distribuidor no existe")
        print("----------------")
        print("")
        cargar_menu_distribuidores(data)

        print("----------------")
        print("1 - Cambio de tiempo")
        print("2 - Cambio de direccion")
        print("3 - Dar de baja")
        print("0 - Salir")
        opcion = es_entero("Selecciona una opcion: ")

        while opcion > 3:
            print("El valor introducido no pertenece al menu")
            opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        previo = data['distribuidores'][ref]['tiempo']
        data['distribuidores'][ref]['tiempo'] = es_entero("Cantidad: ")
        print("Tiempo actualizado, valor anterior: " + str(previo) + " valor actual: " + str(
            data['distribuidores'][ref]['tiempo']))
    elif opcion == 2:
        previo = data['distribuidores'][ref]['direccion']
        data['distribuidores'][ref]['direccion'] = alfa_numerico("Dirección: ")
        print("Dirección actualizado, valor anterior: " + str(previo) + " valor actual: " + str(
            data['distribuidores'][ref]['direccion']))
    elif opcion == 3:
        data['distribuidores'].pop(ref)

    menu.cargar_menu(data)

# Funcion que renderiza las opciones de modificacion.

def modificacion_distribuidores(data):
    print("----------------")
    print("")
    print("Modificar Distribuidor")
    print("1 - Ingresar una referencia")
    print("2 - Listar distribuidores")

    opcion = es_entero("Selecciona una opcion: ")
    while opcion > 2:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        modificar_distribuidor(data)
    elif opcion == 2:
        sistema.cargar_listado_distribuidores(data)
