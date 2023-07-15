"""
@author: CARLOS ANDRES YANEZ CORREA
"""

from utils import es_entero, limpiar_pantalla
import menu
import componentes
import distribuidores
import equipos


def cargar_menu_sistema(data):
    limpiar_pantalla()
    print("--- MENU SISTEMA ---")
    print("")
    print("  1 - Distribuidores")
    print("  2 - Componentes")
    print("  3 - Equipos")
    print("  0 - Salir")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: " )

    while opcion > 3:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        cargar_listado_distribuidores(data)
    elif opcion == 2:
        cargar_listado_componentes(data)
    elif opcion == 3:
        cargar_listado_equipos(data)


def cargar_listado_equipos(data):

        print("")
        for clave, valor in data['equipos'].items():
            print(f"Nombre: {clave}, Fuente: {data['equipos'][clave]['fuente']}, PB: {data['equipos'][clave]['placa_base']}")

        print("Deseas introducir otro equipo?")
        print("1 - SI")
        print("0 - NO")
        print("")
        opcion = es_entero("Selecciona una opcion: ")

        while opcion > 1:
            print("El valor introducido no pertenece al menu")
            opcion = es_entero("Selecciona una opcion: ")

        if opcion == 1:
            equipos.cargar_menu_equipos(data)
        else:
           menu.cargar_menu(data)

def cargar_listado_componentes(data):

    print("")
    for clave, valor in data['componentes'].items():
        print(f"Nombre: {clave}, Cantidad: {data['componentes'][clave]['cantidad']}, Coste: {data['componentes'][clave]['coste']}")

    print("")
    print("Deseas introducir otro componente?")
    print("1 - SI")
    print("0 - NO")
    print("")
    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 1:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        componentes.alta_componentes(data)
    else:
        menu.cargar_menu(data)

def cargar_listado_distribuidores(data):

    print("")
    for clave, valor in data['distribuidores'].items():
        print(f"Nombre: {clave}, Direccion: {data['distribuidores'][clave]['direccion']}, Tiempo: {data['distribuidores'][clave]['tiempo']}")


    print("")
    print("Deseas introducir otro distribuidor?")
    print("1 - SI")
    print("0 - NO")
    print("")

    opcion = es_entero("Selecciona una opcion: ")

    while opcion > 1:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
        distribuidores.alta_distribuidores(data)
    else:
        menu.cargar_menu(data)