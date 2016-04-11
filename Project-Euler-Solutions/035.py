#Problem 35:
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves #prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

import sympy as sp
def cirShift(num):
    num = int(str(num)[1:] + str(num)[:1])
    return num

def main():
    count = 0
    arr = []
    for i in range(1,1000000,2):
        if(sp.isprime(i) == True):
            summa = 0
            length = len(str(i))
    
            for j in range(0,length):
                if(sp.isprime(i) == True):
                    summa += 1
                i = cirShift(i)
                
            if(summa == length):
                count += 1
                if(sp.isprime(i) == True):
                    arr.append(i)
                    
  
    #Adding one because 2 is also a circular prime number
    print len(list(set(arr)))+1
    
main()
