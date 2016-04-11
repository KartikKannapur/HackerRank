def isPalin(num):
    if(str(num) == str(num)[::-1]):
        return True
    else:
        return False

    
def main():
    t = int(input())
    
    for i in range(t):
        num = input()
        num += 1
        
        if(isPalin(num)):
            print num
            
        while(isPalin(num) == False):
            num += 1
            
            if(isPalin(num)):
                print num
                
            
            
        
main()
