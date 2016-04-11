#Problem 45:
#Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
#Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
#It can be verified that T285 = P165 = H143 = 40755.
#Find the next triangle number that is also pentagonal and hexagonal.

import sympy as sp

def tri(n):
    return ((n*(n+1))/2)
    
def pent(n):
    return ((n*((3*n)-1))/2)
    
def hex(n):
    return (n*((2*n)-1))

def main():
    count = 0
    tri_arr = []
    pent_arr = []
    hex_arr = []
    
    for i in range(0,200001):
        tri_arr.append(tri(i))
        pent_arr.append(pent(i))
        hex_arr.append(hex(i))
    
    print list(set(tri_arr) & set(pent_arr) & set(hex_arr))[-1]
  
  
main()
    
