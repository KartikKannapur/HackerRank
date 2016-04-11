#Problem 28:
#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13
#It can be verified that the sum of the numbers on the diagonals is 101.
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def main():
    #num has to be an odd number
    num = 1001
    val_even = 0
    val_odd = 1
    
    summa = []
    for i in range(1,num+1):
        if(i%2==1):
            summa.append(i**2)
            summa.append((i**2)+1+val_odd)
            val_odd += 2
        if(i%2==0):
            val_even += 2
            summa.append((i**2)+1)
            summa.append((i**2)+1+val_even)
    
    total = 0
    for i in summa:
        if(i <= (num**2)):
            total += i
            
    print total
    
main()
