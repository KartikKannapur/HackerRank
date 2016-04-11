#Problem 4:
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers #is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalin(num):
    if(num == int(str(num)[::-1])):
        return True
        
def main():
    arr = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            prod = i*j
            if(isPalin(prod) == True):
                arr.append(prod)
    arr.sort()
    print arr[-1]
main()
