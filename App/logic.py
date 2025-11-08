import time
import csv
from DataStructures import array_list as lt
from DataStructures import binary_search_tree as bst
from DataStructures import map_linear_probing as mlp
from datetime import datetime

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalogo = {}

    #Lista de vuelos completos
    catalogo["lista_vuelos"] = lt.new_list()

    return catalogo


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    if filename == 1:
        filename = "Data/flights_test.csv"
    elif filename == 2:
        filename = "Data/flights_small.csv"
    elif filename == 3:
        filename = "Data/flights_medium.csv"
    elif filename == 4:
        filename = "Data/flights_large.csv"
    else:
        raise Exception("Error - No hay archivo partiendo del parametro ingresado")
    

    data_vuelos = list(csv.DictReader(open(filename,mode="r",encoding="utf-8")))

    for vuelo in data_vuelos:

        vuelo["date"] = datetime.strptime(vuelo["date"],"%Y-%m-%d")
        vuelo["dep_time"] = datetime.strptime(vuelo["dep_time"],"%H:%M")
        vuelo["sched_dep_time"] = datetime.strptime(vuelo["sched_dep_time"],"%H:%M")
        vuelo["arr_time"] = datetime.strptime(vuelo["arr_time"],"%H:%M")
        vuelo["sched_arr_time"] = datetime.strptime(vuelo["sched_arr_time"],"%H:%M")
        vuelo["flight"] = int(vuelo["flight"])
        vuelo["air_time"] = float(vuelo["air_time"])
        vuelo["distance"] = int(vuelo["distance"])

        lt.add_last(catalog["lista_vuelos"],vuelo)


    return catalog


def sort_criteria_load_data(data_1,data_2):

    if data_1["date"] > data_2["date"]:
        return 1
    elif data_1["date"] < data_2["date"]:
        return -1
    else:
        if data_1["sched_dep_time"] > data_2["sched_dep_time"]:
            return 1
        elif data_1["sched_dep_time"] < data_2["sched_dep_time"]:
            return -1
        else:
            return 0


def load_data_present_info(catalog):

    lista_vuelos = catalog["lista_vuelos"]

    lista_vuelos = lt.merge_sort(lista_vuelos,cmp_function=sort_criteria_load_data)

    lista_tabulate = []

    sublista_1 = lt.sub_list(lista_vuelos,0,5)

    sublista_2 = lt.sub_list(lista_vuelos,lt.size(lista_vuelos)-5,5)

    for registro_1 in sublista_1["elements"]:

        registro_1_arreglado = {}

        registro_1_arreglado["fecha_vuelo"] = registro_1["date"].strftime("%Y-%m-%d")
        registro_1_arreglado["hora_salida_real"] = registro_1["dep_time"].strftime("%H:%M")
        registro_1_arreglado["hora_llega_real"] = registro_1["arr_time"].strftime("%H:%M")
        registro_1_arreglado["codigo_aerolinea"] = registro_1["carrier"]
        registro_1_arreglado["nombre_aerolinea"] = registro_1["name"]
        registro_1_arreglado["identificador_aeronave"] = registro_1["tailnum"]
        registro_1_arreglado["codigo_origen"] = registro_1["origin"]
        registro_1_arreglado["codigo_destino"] = registro_1["dest"]
        registro_1_arreglado["distancia_millas"] = registro_1["distance"]
        registro_1_arreglado["duracion_minutos"] = registro_1["air_time"]

        lista_registro_1_arreglado = list(registro_1_arreglado.values())
        lista_tabulate.append(lista_registro_1_arreglado)


    for registro_2 in sublista_2["elements"]:

        registro_2_arreglado = {}

        registro_2_arreglado["fecha_vuelo"] = registro_2["date"].strftime("%Y-%m-%d")
        registro_2_arreglado["hora_salida_real"] = registro_2["dep_time"].strftime("%H:%M")
        registro_2_arreglado["hora_llega_real"] = registro_2["arr_time"].strftime("%H:%M")
        registro_2_arreglado["codigo_aerolinea"] = registro_2["carrier"]
        registro_2_arreglado["nombre_aerolinea"] = registro_2["name"]
        registro_2_arreglado["identificador_aeronave"] = registro_2["tailnum"]
        registro_2_arreglado["codigo_origen"] = registro_2["origin"]
        registro_2_arreglado["codigo_destino"] = registro_2["dest"]
        registro_2_arreglado["distancia_millas"] = registro_2["distance"]
        registro_2_arreglado["duracion_minutos"] = registro_2["air_time"]

        registro_2_arreglado_list = list(registro_2_arreglado.values())
        lista_tabulate.append(registro_2_arreglado_list)


    return lista_tabulate

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
