"""
@author: CARLOS ANDRES YANEZ CORREA
"""


import menu

from utils import es_entero, alfa_numerico, es_float, limpiar_pantalla
from sistema import cargar_listado_componentes

# Renderiza el menu de componentes
def cargar_menu_componentes(data):
    limpiar_pantalla()
    print("--- MENU COMPONENTES ---")
    print("")
    print("  1 - Alta")
    print("  2 - Modificación")
    print("  0 - Salir")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 2:
       print("El valor introducido no pertenece al menu")
       opcion = es_entero("Selecciona una opcion: ")

    seleccionar_opcion(opcion, data)

# Selecciona la opcion del menu de componentes
def seleccionar_opcion(opcion, data):
    if opcion == 1:
        alta_componentes(data)
    elif opcion == 2:
        modificacion_componentes(data)
    else:
        menu.cargar_menu(data)

# Renderiza el menu de modificacion de componentes

def modificacion_componentes(data):
    print("----------------")
    print("")
    print("Modificar Componente")
    print("1 - Ingresar una referencia")
    print("2 - Listar componentes")
    opcion = es_entero("Selecciona una opcion: ")
    while opcion > 2:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        modificar_componente(data)
    elif opcion == 2:
        cargar_listado_componentes(data)


# Permite modificar el stock, la informacion o dar de baja un componente

def modificar_componente(data):
    limpiar_pantalla()
    print("----------------")
    ref = alfa_numerico("Identificador (único): ")
    if ref not in data['componentes']:
        limpiar_pantalla()
        print("La referencia no existe")
        print("----------------")
        print("")
        cargar_menu_componentes(data)

    print("----------------")
    print("1 - Cambio Stock")
    print("2 - Cambio información")
    print("3 - Dar de baja")
    print("0 - Salir")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 3:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
       previo = data['componentes'][ref]['cantidad']
       data['componentes'][ref]['cantidad'] = es_entero("Cantidad: ")
       print("Stock actualizado, valor anterior: " + str(previo) + " valor actual: " + str(data['componentes'][ref]['cantidad']))
    elif opcion == 2:
        data['componentes'][ref]['tipo'] = seleccionar_tipo_componente()
        data['componentes'][ref]['peso'] = es_entero("Peso: ")
        data['componentes'][ref]['coste'] = es_float("Coste: ")
    elif opcion == 3:
        data['componentes'].pop(ref)

    menu.cargar_menu(data)

# Funcion que permite crear un componente nuevo
def alta_componentes(data):
    limpiar_pantalla()
    print("----------------")
    print("")
    print("Alta Componentes")
    ref = alfa_numerico("Identificador (único): ")

    if ref in data['componentes']:
        limpiar_pantalla()
        print("La referencia ya existe")
        cargar_menu_componentes(data)

    tipo = seleccionar_tipo_componente()

    peso = es_entero("Peso: ")
    while peso <= 0:
        print("El peso debe ser mayor que 0")
        peso = es_entero("Peso: ")

    coste = es_float("Coste: ")
    while coste <= 0:
        print("El coste debe ser mayor que 0")
        coste = es_float("Coste: ")

    cantidad = es_entero("Cantidad: ")
    while cantidad <= 0:
        print("La cantidad debe ser mayor que 0")
        cantidad = es_entero("Cantidad: ")

    data['componentes'][ref] = {
        'tipo': tipo,
        'peso': peso,
        'coste': coste,
        'cantidad': cantidad
    }

    print("Componente dado de alta correctamente")
    print("")
    print("Deseas introducir otro componente? 1 : SI  0 : NO")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 1:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        alta_componentes(data)
    else:
        menu.cargar_menu(data)

# Funcion que renderiza el listado de componente para su sleccion.
def seleccionar_tipo_componente():
    print("")
    print("1 - Fuente")
    print("2 - PB")
    print("3 - TG")
    print("4 - CPU")
    print("5 - RAM")
    print("6 - Disco")
    print("")
    tipo = es_entero("Selecciona una opcion: ")
    while tipo > 6:
        print("El valor introducido no pertenece al menu")
        tipo = es_entero("Selecciona una opcion: ")

    return tipo
