#Problem 3:
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math
def isPrime(a):
    return all(a % i for i in xrange(2, a))
            
def main(num):
    arr = []
    for i in range(2,int(math.sqrt(num))+2):
        if((num % i) == 0):
            if(isPrime(i)):
                arr.append(i)
    print arr[-1]
    
main(600851475143)
