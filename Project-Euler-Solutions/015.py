#Problem 15
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly #6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
#Lattice path - The number of paths through a given lattice, with pre-defined
#conditions regarding which path to take.
#such as - Move only right and down

#Pattern:
#For a nxn lattice path, the numbr of possible combinations is 2nCn, where C is
#the number of combinations
#2x2 = 20
#3x3 = 20
#4x4 = 70 so on
def latticePath(n):
    return ((factorial(2*n))/(factorial(n))**2)

print latticePath(20)
