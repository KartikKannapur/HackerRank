__author__ = "Kartik Kannapur"

T = raw_input()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
for i in range(0, int(T)):
	print factorial(int(raw_input()))
