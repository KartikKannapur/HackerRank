def format():
    text = ""
    stopword = ""
    while True:
        line = raw_input()
        if line.strip() == stopword:
            break
        text += "%s\n" % line
    
    text_arr = text.split('\n')
    global arr
    arr = [[] for _ in range(21)]

    for i in range(21):
        arr[i].append(text_arr[i])
        
    #Remove the empty string in the array
    arr.pop(20)
    
    for j in range(20):
        arr[j][0] = arr[j][0].split(' ')
    #List created - arr[i][0][j]
    
    #Convert all numbers to integers
    for a in range(20):
        for b in range(20):
            arr[a][0][b] = int(arr[a][0][b])

def main():
    
    format()
    
    global arr
    greatest = 0
 
    
    for i in range(20):
        for j in range(16):
            # horizontal products
            prod = arr[i][0][j]*arr[i][0][j+1]*arr[i][0][j+2]*arr[i][0][j+3]
            if prod > greatest: 
                greatest = prod
            # vertical products
            prod = arr[j][0][i]*arr[j+1][0][i]*arr[j+2][0][i]*arr[j+3][0][i]
            if prod > greatest: 
                greatest = prod
 
    # diagonal products
    for i in range(16):
        for j in range(16):
            prod = arr[i][0][j]*arr[i+1][0][j+1]*arr[i+2][0][j+2]*arr[i+3][0][j+3]
            if prod > greatest: 
                greatest = prod
    for i in range(3,20):
        for j in range(16):
            prod = arr[i][0][j]*arr[i-1][0][j+1]*arr[i-2][0][j+2]*arr[i-3][0][j+3]
            if prod > greatest: 
                greatest = prod
    
    print greatest
    
            
                                                       
main()
