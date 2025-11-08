

def new_node(key, value):

    new_node = {"key":key,
                "value":value,
                "size":1,
                "left":None,
                "right":None}
    

    return new_node


def get_value(my_node):

    return my_node["value"]

def get_key(my_node):

    return my_node["key"]