def reverse(num):
    return int(str(num)[::-1])



def main():
    t = int(input())
    
    for i in range(t):
        a, b = raw_input().split()
        a = int(a)
        b = int(b)
        
        print int(str((int(str(a)[::-1]) + int(str(b)[::-1])))[::-1]) 
        
    
main()
