from datetime import datetime
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def process_executor(all_primes):
    print("using process....")
    start = datetime.now()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        print(executor._max_workers)
        for number, prime in zip(PRIMES, executor.map(is_prime, all_primes)):
            print('%d is prime: %s' % (number, prime))
            print(executor._processes)
    end = datetime.now() - start
    print(end)

def looping(all_primes):
    print("\nlooping....")
    start = datetime.now()
    for x in all_primes:
        res = is_prime(x)
        print('%d is prime: %s' % (x, res))
    end = datetime.now() - start
    print(end)


def thread_executor(all_primes):
    print("\nusing thread....")
    start = datetime.now()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        print(executor._max_workers)
        for number, prime in zip(PRIMES, executor.map(is_prime, all_primes)):
            print('%d is prime: %s' % (number, prime))
    end = datetime.now() - start
    print(end)


process_executor(PRIMES)
looping(PRIMES)
thread_executor(PRIMES)
