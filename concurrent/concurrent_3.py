from datetime import datetime
import concurrent.futures
import math

""""
ProcessPoolExecutor with submit()
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


def future_stats(future):
    print("done: {}".format(future.done()))
    print("running: {}".format(future.running()))
    print("cancelled: {}".format(future.cancelled()))

def call_output(futures_map):
    for future, v in futures_map.items():
        try:
            print("\n")
            print(future.result())
            future_stats(future)
        except Exception as exp:
            print(future.exception())

with concurrent.futures.ProcessPoolExecutor() as executor:
    prime_futures = {executor.submit(is_prime, prime): prime[1] for prime in PRIMES}
    call_output(prime_futures)
