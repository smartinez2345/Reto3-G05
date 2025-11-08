def is_prime(n):

    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    candidate = n+1 
    while not is_prime(candidate):
        candidate += 1
    return candidate

def hash_value(my_table, key):

    # MAD: (abs(a * hash_key + b) % p) % m, donde:

    a = my_table["scale"]

    b = my_table["shift"]

    m = my_table["capacity"]

    p = next_prime(m)

    hash_key = hash(key)

    result = (abs(a * hash_key + b) % p) % m

    return result #posicion en la lista 


