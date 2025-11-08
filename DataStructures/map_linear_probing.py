
import DataStructures.map_functions as mf

import DataStructures.map_entry as mp

import random

import DataStructures.array_list as lt



def new_map(num_elements, load_factor, prime=109345121):

    capacity = mf.next_prime(int(num_elements/load_factor))

    scale = random.randint(1,prime-1)

    shift = random.randint(0,prime-1)

    new_map = {"capacity":capacity,
               "scale":scale,
               "shift":shift,
               "prime":prime,
               "table": lt.new_list(),
               "current_factor":0,
               "limit_factor":load_factor,
               "size":0}
    
    for i in range(0,capacity):

        lt.add_last(new_map["table"],mp.new_map_entry(None,None))

    return new_map


def is_available(table, pos):
   entry = lt.get_element(table, pos)
   if mp.get_key(entry) is None or mp.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == mp.get_key(entry):
      return 0
   elif key > mp.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   counter = 0
   first_avail = None #variable donde se va a guardar la primera posicion disponible para alojar un value en la tabla de hash (lista)
   found = False #centinela que me marca si se encontro o no se encontro una posicion disponible
   ocupied = False #centinela que me marca si la posicion que se encontro con respecto al hash_value de la key esta ocupada o no
   while not found: #mientras no se haya encontrado una posicion disponible
      if is_available(my_map["table"], hash_value): #caso en que no hay colision por que la posicion -> hash_value esta disponible
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if mp.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0: #caso contrario en el que la posicion -> hash_value no esta disponible por que el key ya esta en ese entry
            first_avail = hash_value
            counter += 1
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"] #Manejo de Colision (Sondeo Lineal) -> cambiar la posicion -> hash_value para que en algun momento se cumpla la funcion is_available y poder ingresar informacion en una posicion libre
   return ocupied, first_avail


def put(my_map, key, value):

    index = mf.hash_value(my_map,key)

    ocupied, first_avail = find_slot(my_map,key,index)

    entry = lt.get_element(my_map["table"],first_avail)

    if ocupied != True: #La llave no estaba en el mapa

        mp.set_key(entry,key)

        mp.set_value(entry,value)

        my_map["size"] += 1

    else: #La llave si estaba en el mapa y solo se actualiza el value

        mp.set_value(entry,value)
    
    my_map["current_factor"] = my_map["size"]/my_map["capacity"]

    if my_map["current_factor"] > my_map["limit_factor"]:

        my_map = rehash(my_map)

    return my_map


def contains(my_map, key):

    value = is_available(my_map["table"],mf.hash_value(my_map,key))

    if value == True: #posicion disponible significa que la llave (key) no esta en la tabla
        return False
    else: #posicion no disponible significa que la llave (key) si esta en la tabla
        return True


def get(my_map, key):

    if contains(my_map,key): #revisar si la llave si se encuentra en la tabla

        pos = mf.hash_value(my_map,key) #posicion en la lista my_map["table"] partiendo de la funcion hash_value aplicada a key

        table = my_map["table"] #lista

        entry = lt.get_element(table,pos)

        return mp.get_value(entry)

    return None


def size(my_map):

    return my_map["size"]


def is_empty(my_map):

    return size(my_map) == 0

def rehash(my_map):

    capacity_original = my_map["capacity"]

    table_original = my_map["table"]

    new_capacity = mf.next_prime(capacity_original*2) #obtuvimos la nueva capacidad de la tabla

    new_table = lt.new_list() #generamos la nueva tabla

    for _ in range(0,new_capacity): #introducimos los diccionarios de tipo map_entry en las posiciones de la nueva tabla partiendo del nuevo capacity

        lt.add_last(new_table,mp.new_map_entry(None,None))

    for j in range(0,capacity_original): #iteramos sobre los diccionarios de tipo map_entru en las posiciones de la tabla vieja 
        
        entry = lt.get_element(table_original,j) #obtenemos cada uno de los diccionarios que estan en la pos = j

        if mp.get_value(entry) != None and mp.get_key(entry) != None: #en caso de que el diccionario de tipo map_entry no este vacio, lo agregamos en la pos = j en la nueva tabla

            new_table[j] = entry

    my_map["capacity"] = new_capacity #asignar la nueva capacidad al mapa

    my_map["table"] = new_table #asignar la nueva tabla al mapa

    my_map["current_factor"] = my_map["size"]/my_map["capacity"] #volver a calcular el current_factor

    return my_map
            

def key_set(my_map):

    key_list = lt.new_list()

    table = my_map["table"]

    for index in range (0,lt.size(table)):

        map_entry = lt.get_element(table,index)

        key = mp.get_key(map_entry)

        if key != None:

            lt.add_last(key_list,key)

    return key_list


def value_set(my_map):

    value_list = lt.new_list()

    table = my_map["table"]

    for index in range (0,lt.size(table)):

        map_entry = lt.get_element(table,index)

        value = mp.get_value(map_entry)

        if value != None:

            lt.add_last(value_list,value)

    return value_list
    

    

