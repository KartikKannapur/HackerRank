def main():
    arr = []
    
    while True:
        num = input()
        
        if(num == 42):
            break
        else:
            arr.append(num)
                
    for i in arr:
        print i
            
main()
