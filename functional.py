from sympy import isprime
from math import factorial
from itertools import repeat, imap

def prove_factorial_divides_by_n_primes(n):
    ''' Always returns True because a factorial
        is divisible by the all primes below n
        by definition'''
    return all(imap(lambda x, y: x % y == 0,
                    repeat(factorial(n)),
                    [y for y in range(1, n) if isprime(y)]))

all(map(prove_factorial_divides_by_n_primes, range(1, 542))) #covers first 100 primes