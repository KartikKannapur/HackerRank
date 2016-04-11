def main():
    t = int(input())
    
    for i in range(t):
        a, b = raw_input().split()
        a = int(a)
        b = int(b)
    
        if(str(b) in str(a)):
            print 1
        else:
            print 0
        
        
main()
