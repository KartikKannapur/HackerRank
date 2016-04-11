def isPrime(num):
    
    if num == 1:
        return False
            
    for i in range(2, num):
        if num % i == 0:
            return False
            
    return True
        
def factors(a,b):
    arr = []
    for i in range(a,b+1):
        if(isPrime(i)):
            arr.append(i)
    for i in arr:
        print i

def main():
    '''main function is used to define the number of test cases & call the isPrime Function'''
    t = int(input())
    
    for i in range(t):
        a, b = raw_input().split()
        a = int(a)
        b = int(b)
    
        factors(a,b)
        
main()
