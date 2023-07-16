"""
@author: CARLOS ANDRES YANEZ CORREA
"""

import os
import menu

from utils import es_entero, alfa_numerico, limpiar_pantalla

def cargar_menu_equipos(data):
    limpiar_pantalla()
    print("--- MENU EQUIPOS ---")
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

def seleccionar_opcion(opcion, data):
    if opcion == 1:
        alta_equipos(data)
    elif opcion == 2:
        modificacion_equipos(data)
    else:
        menu.cargar_menu(data)

def alta_equipos (data):
    limpiar_pantalla()
    print("----------------")
    print("")
    print("Alta equipos")
    ref = alfa_numerico("Identificador (único): ")
    validar_ref(ref, data)
    agregar_componentes(ref, data)


def agregar_componentes(ref, data):

    ## Cargamos el listado de componentes filtrando solo los componentes de tipo fuente
    print("----------------")
    fuentes = {k: v for k, v in data['componentes'].items() if v["tipo"] == 1 and v["cantidad"] > 1}
    for clave, valor in fuentes.items():
        print(f"Nombre: {clave}, Cantidad: {data['componentes'][clave]['cantidad']}, Coste: {data['componentes'][clave]['coste']}")
    ref_fuente = alfa_numerico("Identificador fuente (único): ")

    ## Cargamos el listado de componentes filtrando solo los componentes de tipo placa base
    print("----------------")
    pbs = {k: v for k, v in data['componentes'].items() if v["tipo"] == 2 and v["cantidad"] > 1}
    for clave, valor in pbs.items():
        print(f"Nombre: {clave}, Cantidad: {data['componentes'][clave]['cantidad']}, Coste: {data['componentes'][clave]['coste']}")
    ref_pb = alfa_numerico("Identificador placa base (único): ")

    ## Cargamos el listado de componentes filtrando solo los componentes de tipo TG
    print("----------------")
    tgs = {k: v for k, v in data['componentes'].items() if v["tipo"] == 3 and v["cantidad"] > 1}
    for clave, valor in tgs.items():
        print(f"Nombre: {clave}, Cantidad: {data['componentes'][clave]['cantidad']}, Coste: {data['componentes'][clave]['coste']}")
    ref_tg = alfa_numerico("Identificador tg (único): ")

    ## Cargamos el listado de componentes filtrando solo los componentes de tipo CPU
    print("----------------")
    cpus = {k: v for k, v in data['componentes'].items() if v["tipo"] == 4 and v["cantidad"] > 1}
    for clave, valor in cpus.items():
        print(f"Nombre: {clave}, Cantidad: {data['componentes'][clave]['cantidad']}, Coste: {data['componentes'][clave]['coste']}")
    ref_cpu = alfa_numerico("Identificador cpu (único): ")

    ## Cargamos el listado de componentes filtrando solo los componentes de tipo RAM
    print("----------------")
    rams = {k: v for k, v in data['componentes'].items() if v["tipo"] == 5 and v["cantidad"] > 1}
    for clave, valor in rams.items():
        print(f"Nombre: {clave}, Cantidad: {data['componentes'][clave]['cantidad']}, Coste: {data['componentes'][clave]['coste']}")
    ref_ram = alfa_numerico("Identificador ram (único): ")

    ## Cargamos el listado de componentes filtrando solo los componentes de tipo disco
    print("----------------")
    discos = {k: v for k, v in data['componentes'].items() if v["tipo"] == 6 and v["cantidad"] > 1}
    for clave, valor in discos.items():
        print(f"Nombre: {clave}, Cantidad: {data['componentes'][clave]['cantidad']}, Coste: {data['componentes'][clave]['coste']}")
    ref_disco = alfa_numerico("Identificador disco (único): ")


    ## Descontamos el stock de cada uno de los componentes usados en el equipo
    data['componentes'][ref_fuente]['cantidad'] -= 1
    data['componentes'][ref_pb]['cantidad'] -= 1
    data['componentes'][ref_tg]['cantidad'] -= 1
    data['componentes'][ref_cpu]['cantidad'] -= 1
    data['componentes'][ref_ram]['cantidad'] -= 1
    data['componentes'][ref_disco]['cantidad'] -= 1

    ## Almacenamos el equipo
    data['equipos'][ref] = {
        "fuente": ref_fuente,
        "placa_base": ref_pb,
        "tg": ref_tg,
        "cpu": ref_cpu,
        "ram": ref_ram,
        "disco": ref_disco,
        "cantidad": 1
    }

    print("Equipo agregado correctamente")
    cargar_menu_equipos(data)

def agegar_fuente(data):
    print("----------------")
    print("")
    print("Agregar fuente")
    print("1 - Ingresar una referencia")
    print("2 - Listar fuentes")
    print("0 - Salir")

    opcion = es_entero("Selecciona una opcion: ")
    while opcion > 2:
        print("El valor introducido no pertenece al menu")
        opcion = es_entero("Selecciona una opcion: ")

    if opcion == 1:
      ref_fuente = alfa_numerico("Identificador fuente (único): ")
      return ref_fuente
    elif opcion == 2:
        print("Listar fuentes")
    else:
        cargar_menu_equipos(data)



def validar_ref(ref, data):
    if ref in data['equipos']:
        limpiar_pantalla()
        print("La referencia ya existe")
        cargar_menu_equipos(data)

def modificacion_equipos(data):
    print("Modificacion equipos")
