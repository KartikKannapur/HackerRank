def main():
    arr = []
    global maxx
    maxx = 0
    for num in range(1,1000001):
        count = 0
        i = num
        while(i != 1):
            if(i % 2 == 0):
                i = i/2
                count += 1
                continue
            if(i % 2 == 1):
                i = ((3*i) + 1)
                count += 1
                continue
        count += 1
        if(count > maxx):
            maxx = count
            arr.append(num)
    print arr[-1]
        
main()
        
