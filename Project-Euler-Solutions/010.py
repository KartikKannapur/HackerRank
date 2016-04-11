#Problem 10:
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import sympy as sp

def main():
    summa = 0
    for i in range(1,2000001):
        if(sp.isprime(i)):
            summa += i
            
    print summa
                                            
main()
