#Problem 33:
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may #incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two #digits in the numerator and denominator.
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import fractions as fr

def main():
    out = []
    ans = 1
    num_prod = 1
    deno_prod = 1
    for num in range(10,100):
        for deno in range(10,100):
            arr = []
            arr_val = []
            if(num < deno):
                if(len(list(set(list(str(num)))&set(list(str(deno))))) == 1):
                    arr = (list(set(list(str(num)))^set(list(str(deno)))))
                    for i in range(0,len(arr)):
                        arr_val.append(int(arr[i]))
                    arr_val.sort()
                    if(len(arr_val) == 2):
                        if(arr_val[1] != 0):
                            if(num % 10 != 0):
                                if(deno % 10 != 0):
                                    div_new = float(arr_val[0])/float(arr_val[1])
                                    div_ori = float(num)/float(deno)
                                    if(div_new == div_ori):
                                        if(int(str(num)[::-1]) < deno):
                                            m = fr.Fraction(num,deno)
                                            num_prod *= m.numerator
                                            deno_prod *= m.denominator
                                            
    #print num_prod,deno_prod
    g = fr.Fraction(num_prod,deno_prod)
    print g.denominator
                                            
main()
