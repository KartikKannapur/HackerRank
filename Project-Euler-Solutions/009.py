#Problem 9:
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#a<b<c
def isPytha(a,b,c):
    if(((a*a)+(b*b)) == (c*c)):
        return True
  
def main():  
    for i in range(1,1000):
        for j in range(1,1000):
            k = 1000 - (i+j)
            if(isPytha(i,j,k)):
                print i*j*k
                        
main()
