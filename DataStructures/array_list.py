def new_list():

    new_array = {"elements":[],
                 "size":0}
    return new_array


def is_empty(my_list):
    return my_list["size"] == 0

def size(my_list):
    return my_list["size"]

def add_last(my_list,element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def add_first(my_list,element):
    my_list["elements"].insert(0,element)
    my_list["size"] += 1
    return my_list

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][0]
    
def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][size(my_list)-1]


def get_element(my_list,pos):

    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][pos]
    

def delete_element(my_list,pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"].pop(pos)

def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"].pop(0)

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"].pop(size(my_list)-1)

def insert_element(my_list, element, pos):
    if is_empty(my_list):
         my_list["elements"].insert(0,element)
    else:
        my_list["elements"].insert(pos,element)
    my_list["size"] += 1
    return my_list

def default_function(elemen_1, element_2):

   if elemen_1 > element_2:
      return 1 #mayor que
   elif elemen_1 < element_2:
      return -1 #menor que
   return 0 #igual que

def is_present(my_list, element, cmp_function=default_function): #O(n)
    if is_empty(my_list): #O(1)
        return -1 #O(1)
    else: #O(1)
        i = 0 #O(1)
        found = False #O(1)
        while i < size(my_list) and found == False: #O(n)
            value_cmp = cmp_function(element,my_list["elements"][i]) #O(1)
            if value_cmp == 0: #O(1)
                found = True #O(1)
            else: #O(1)
                i += 1 #O(1)
        if found:
            return i
        else:
            return -1

def change_info(my_list, pos, new_info):
    
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")

    my_list["elements"][pos] = new_info
    return my_list

def merge_sort(my_list, cmp_function=default_function):
    """
    Ordena la lista my_list usando MergeSort.
    Retorna una nueva lista ordenada (no modifica la original).
    """

    # Caso base: listas de tamaño 0 o 1 ya están ordenadas
    if size(my_list) <= 1:
        return my_list

    mid = size(my_list) // 2

    # Dividir la lista en dos mitades
    left_half = {"elements": my_list["elements"][:mid], "size": mid}
    right_half = {"elements": my_list["elements"][mid:], "size": size(my_list) - mid}

    # Ordenar recursivamente cada mitad
    left_sorted = merge_sort(left_half, cmp_function)
    right_sorted = merge_sort(right_half, cmp_function)

    # Mezclar resultados
    return merge(left_sorted, right_sorted, cmp_function)


def merge(left, right, cmp_function):
    """
    Fusiona dos listas ordenadas (left y right) en una nueva lista ordenada.
    """
    result = new_list()
    i, j = 0, 0

    while i < size(left) and j < size(right):
        if cmp_function(left["elements"][i], right["elements"][j]) <= 0:
            add_last(result, left["elements"][i])
            i += 1
        else:
            add_last(result, right["elements"][j])
            j += 1

    # Agregar los elementos restantes
    while i < size(left):
        add_last(result, left["elements"][i])
        i += 1
    while j < size(right):
        add_last(result, right["elements"][j])
        j += 1

    return result


def sub_list(my_list, i, n):
    """
    Retorna una sublista de my_list que empieza en la posición i
    y contiene hasta n elementos (o menos si no hay suficientes).
    """
    if i < 0 or i >= size(my_list):
        raise IndexError("list index out of range")

    # límite final, no mayor que size(my_list)
    end = min(i + n, size(my_list))

    # Crear nueva lista con el rango especificado
    new_array = {"elements": my_list["elements"][i:end], 
                 "size": end - i}
    return new_array