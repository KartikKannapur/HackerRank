def loop(num):
    summa = 0
    arr = list(str(num))
    for k in range(0,len(arr)):
        summa += int(arr[k])**2
    return summa
    
def main():
    count = 0
    for i in range(1,10000001):
        m = i
        arr = []    
        while(1):
            m = loop(m)
            arr.append(m)
            if(1 in arr):
                break
            if(89 in arr):
                count += 1
                break
    print count
            
        
main()
