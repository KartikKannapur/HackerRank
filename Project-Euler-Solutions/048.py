#Problem 48:
#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

import math

def main():
    summa = 0
    for i in range(1,1001):
        summa += pow(i,i,10**10)
    print int(str(summa)[-10:])
main()
    
