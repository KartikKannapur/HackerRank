#Problem 40:
#An irrational decimal fraction is created by concatenating the positive integers:
#0.123456789101112131415161718192021...
#It can be seen that the 12th digit of the fractional part is 1.
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def main():
    num = []
    for i in range(1,1000001):
        num.append(str(i))
    val = ''.join(num)
    
    #print val[0]*val[9]*val[99]*val[999]*val[9999]*val[99999]*val[999999]
    print int(val[0])*int(val[9])*int(val[99])*int(val[999])*int(val[9999])*int(val[99999])*int(val[999999])

main()
