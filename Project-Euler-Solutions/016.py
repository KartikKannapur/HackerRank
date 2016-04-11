#Problem 16:
#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 21000?

import math
def main(num):
    val = pow(2,num)
    summa = 0
    val_list = list(str(val))
    
    for i in val_list:
        summa += int(i)
    print summa
    
main(1000)
