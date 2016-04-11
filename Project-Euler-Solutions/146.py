#Problem 146:
#The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive #primes is 10. The sum of all such integers n below one-million is 1242490.
#What is the sum of all such integers n below 150 million?

import math
import sympy as sp

def main():
    summa = 0
    for num in range(1,150000001):
        arr_num = []
        arr_const = [1,3,7,9,13,27]
        
        #List to hold all possible values
        for i in arr_const:
            var = ((num**2)+i)
            if(sp.isprime(var)):
                arr_num.append(var) 
                
        count = len(arr_num)
              
        #Number of primes between two numbers
        count_prime = 0
        for k in range((num**2)+1,(num**2)+27+1):
            if(sp.isprime(k)):
                count_prime += 1
        
        if(count == 6):
            if(count == count_prime):
                print num
                summa += num
            
    print "Total : " + str(summa)
main()
