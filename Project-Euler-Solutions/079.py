#Problem 79:
#A common security method used for online banking is to ask the user for three random characters from a passcode. For #example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: #317.
#The text file, keylog.txt, contains fifty successful login attempts.
#Given that the three characters are always asked for in order, analyse the file so as to determine the shortest #possible secret passcode of unknown length.

def main():
    f = open("PATH\\names.txt")
    fr = f.read()
    fr = fr.split('\n')
    
    #Remove empty string
    del fr[-1]

    #List all numbers 
    arr = []
    for i in range(0,len(fr)):
        arr.extend((fr[i]))
        
    #Convert Str to Int
    for j in range(0,len(arr)): 
        arr[j] = int(arr[j])
    for j in range(0,len(fr)): 
        fr[j] = int(fr[j])

    
    final = list(set(arr))
    final.sort(key=arr.index)

    
    for k in range(0,len(fr)):
        myArr = []
        temp = list(str(fr[k]))
        for p in range(0,len(temp)): 
            temp[p] = int(temp[p])
        
        for h in range(0,2):
            a1 = final.index(temp[h])
            a2 = final.index(temp[h+1])
            if(a1 > a2):
                final[a1],final[a2] = final[a2],final[a1]
    
    for g in range(0,len(final)): 
        final[g] = str(final[g])          
    print ''.join(final)
main()
