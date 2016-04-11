#Problem 7:
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

import sympy as sp
def main():
    count = 0
    for i in range(0,1000000):
        if(sp.isprime(i)):
            count += 1
            if(count == 10001):
                print i
                break
        
    
main()
