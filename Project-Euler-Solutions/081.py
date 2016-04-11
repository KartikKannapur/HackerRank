#Problem 81:
#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right #and down, is indicated in bold red and is equal to 2427.
#(MATRIX)
#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 #by 80 matrix, from the top left to the bottom right by only moving right and down.

def main():
    num = 80
    f = open('Path\\matrix.txt','r')
    fr = f.read()
    arr = fr.split('\n')
    del arr[-1]

    arr_ori = [[0 for i in range(0,num)]for j in range(0,num)]
    
    for i in range(0,len(arr)):
        temp_arr = []
        temp_arr = arr[i].split(',')
        for j in range(0,len(temp_arr)):temp_arr[j] = int(temp_arr[j])
        
        for k in range(0,len(temp_arr)):
            arr_ori[i][k] = (temp_arr[k])
    
 #   arr_ori = [[131, 673, 234, 103, 18],
 #[201, 96, 342, 965, 150],
 #[630, 803, 746, 422, 111],
 #[537, 699, 497, 121, 956],
 #[805, 732, 524, 37, 331]]

    #print arr_ori       
    summa = 0
    i,j = 0,0
    
    for i in range(0,len(arr_ori)):
        for j in range(0,len(arr_ori)):
            
            if(i == j):
                summa += arr_ori[i][j]
                print "Element: " +  str(arr_ori[i][j]) + " Index: " + str(i) +" " + str(j)
            
                
            if(((i - j))==1):
                summa += min(arr_ori[i][j],arr_ori[j][i])
                print "Element: " + str(min(arr_ori[i][j],arr_ori[j][i])) + " Value: " + str(arr_ori[i][j]) + " " + str(arr_ori[j][i])+ " Index: " + str(i) +" " + str(j)
                
        
        print "SUM: " + str(summa)
main()
