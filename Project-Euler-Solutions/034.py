#Problem 34:
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import sympy as sp
def main():
    summa = 0
    for i in range(3,50000):
        sum = 0
        arr = list(str(i))
        for j in arr:
            sum += sp.factorial(int(j))
        if(sum == i):
            #print sum
            summa += sum
    print summa
            
main()
