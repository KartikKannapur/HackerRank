#Problem 6:
#The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is #3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the #sum.

nums = 100

def sumOsq():
    summa = 0
    for i in range(1,nums+1):
        summa += (i*i)
    return summa
    
def sqOsum():
    summa = 0
    for i in range(1,nums+1):
        summa += i
    return summa*summa
    
def main():
    print sqOsum() - sumOsq() 
    
main()
