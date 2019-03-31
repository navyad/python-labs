from datetime import datetime
import concurrent.futures
import math

""""
ProcessPoolExecutor with map()
"""
PRIMES = [ (112272535095293, "one"),
           (112582705942171, "two"),
           (112272535095293, "three"),
           (115280095190773, "four"),
           (115797848077099, "five"),
           (1099726899285419, "six")
         ]

def is_prime(itr):
    n, name = itr

    if name == 'four':
        message = "exception for item: {}".format(name)
        raise Exception(message)

    if n % 2 == 0:
        return False, name

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False, name
    return True, name


def initializer():
    print("init called....")

def call_output(gen):
    for return_val in gen:
        try:
            print(return_val)
        except Exception as exp:
            print(exp.message)


with concurrent.futures.ProcessPoolExecutor(initializer=initializer) as executor:
    gen = executor.map(is_prime, PRIMES)
    call_output(gen)

