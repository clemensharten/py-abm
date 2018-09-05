# Example for using ProcessPoolExecutor in Python for parallel execusion of code.
# Adapted from the Python Documentation: https://docs.python.org/3/library/concurrent.futures.html

import concurrent.futures
import math


PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    1099726899285412,
    1099726899285415,
    1099726899285411]
PRIMES = PRIMES * 5    

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
import time
 

def main():
    then = int(round(time.time()))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    now = int(round(time.time()))
    print(now - then)
    then = now
    for number in PRIMES:
        print('%d is prime: %s' % (number, is_prime(number)))
    now = int(round(time.time()))
    print(now - then)
    then = now   

if __name__ == '__main__':
    main()





