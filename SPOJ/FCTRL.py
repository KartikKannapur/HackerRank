import math

def trail(num):
    val = int(str(num)[::-1])
    print (len(str(num)) - len(str(val)))

def main():
    t = int(input())
    
    for i in range(t):
        num = input()
        fact = math.factorial(num)
        
        trail(fact)
        
    
main()
