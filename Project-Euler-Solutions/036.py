#Problem 36:
#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

def isPalin(num):
    if(num == int(str(num)[::-1])):
        return True
        
def main():
    summa = 0
    for i in range(1,1000000):
        base2 = int(bin(i)[2:])
        base10 = i
        
        if((isPalin(base2) == True) & (isPalin(base10) == True)):
            summa += base10
            
    print summa
main()
