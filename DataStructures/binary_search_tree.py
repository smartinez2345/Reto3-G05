from DataStructures import bst_node 

def new_map():

    new_map = {"root":None}

    return new_map


def put(my_bst, key, value):

    my_bst["root"] = insert_node(my_bst["root"],key,value)

    return my_bst


def size(my_bst):

    return size_tree(my_bst["root"])


def size_tree(root):

    if root is None:
        return 0
    return root["size"]


def insert_node(root,key,value):

    node = bst_node.new_node(key,value)

    if root is None: #Caso en el que se encuentra una posicion vacia 

        return node
    
    if key < bst_node.get_key(root): #la llave que se quiere insertar es mayor al nodo que esta revisando en esa iteracion

        root["left"] = insert_node(root["left"],key,value)
    
    elif key > bst_node.get_key(root): #la llave que se quiere insertar es menor al nodo que se esta revisando en esa iteracion

        root["right"] = insert_node(root["right"],key,value)
    
    else: #la llave que se quiere insertar es igual a la que se esta revisando en esa iteracion

        root["value"] = value

        return root

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])

    return root


def get(my_bst,key):

    return get_node(my_bst["root"],key)


def get_node(root, key):

    if root is None: #No lo encontre
        return None
    
    if bst_node.get_key(root) == key: #Encontre la llave en un nodo
        return root
    
    if bst_node.get_key(root) > key: #La llave del nodo que se esta revisando es mayor a la que se ingreso por parametro nos vamos para el subarbol izquierdo
        return get_node(root["left"],key)
    
    else: #en caso contrario nos vamos para el subarbol derecho
        return get_node(root["right"],key)
    


def remove(my_bst,key):

    return remove_node(my_bst["root"],key)

def remove_node(root,key):


    if root is None:
        return None
    
    if key < bst_node.get_key(root):

        root["left"] = remove_node(root["left"],key)

    elif key > bst_node.get_key(root):

        root["right"] = remove_node(root["right"],key)

    else:

        if root["left"] is None:

            return root["right"]
        
        elif root["right"] is None:

            return root["left"]
        

        succesor = get_min_node(root["right"])

        root["key"] = succesor["key"]
        root["value"] = succesor["value"]

        root["right"] = remove_node(root["right"],succesor["key"])

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])

    return root


def get_min(my_bst):

    return get_min_node(my_bst["root"])

def get_max(my_bst):
    
    return get_max_node(my_bst["root"])


def get_max_node(root):

    current = root
    while current["right"] is not None:
        current = current["right"]
    return current

def get_min_node(root):

    current = root
    while current["left"] is not None:
        current = current["left"]
    return current


def is_empty(my_bst):

    if my_bst["root"] is None:
        return True
    return False


def contains(my_bst,key):
    if get(my_bst,key) == None:
        return False
    return True







    

