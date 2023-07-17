"""
@author: CARLOS ANDRES YANEZ CORREA
"""


from utils import es_entero, limpiar_pantalla
from componentes import cargar_menu_componentes
from distribuidores import cargar_menu_distribuidores
from archivo import cargar_menu_archivos
from sistema import cargar_menu_sistema
from equipos import cargar_menu_equipos
from despachar import cargar_menu_despachar
from dias import cargar_menu_dias
from pprint import pprint

# Funcion que carga el menu principal del programa.
def cargar_menu(data):
    limpiar_pantalla()
    print("--- MENU PRINCIPAL ---")
    print("")
    print("  1 - Componentes")
    print("  2 - Equipos")
    print("  3 - Distribuidores")
    print("  4 - Despachar")
    print("  5 - Días")
    print("  6 - Info sistema")
    print("  7 - Ficheros")
    print("  0 - Salir")
    print("")
    print("-----------------")
    opcion = es_entero("Selecciona una opcion: " )

    while opcion > 8:
       print("El valor introducido no pertenece al menu")
       opcion = es_entero("Selecciona una opcion: ")

    seleccionar_opcion(opcion, data)


def seleccionar_opcion(opcion, data):
    if opcion == 1:
        cargar_menu_componentes(data)
    elif opcion == 2:
        cargar_menu_equipos(data)
    elif opcion == 3:
        cargar_menu_distribuidores(data)
    elif opcion == 4:
        cargar_menu_despachar(data)
    elif opcion == 5:
        cargar_menu_dias(data)
    elif opcion == 6:
        cargar_menu_sistema(data)
    elif opcion == 7:
        cargar_menu_archivos(data)
    elif opcion == 8:
       pprint(data, indent=4)
       cargar_menu(data)
    else:
        print("Gracias por usar nuestro sistema")