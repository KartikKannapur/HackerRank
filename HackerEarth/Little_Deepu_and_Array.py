__author__ = "Kartik Kannapur"

# N = Size of the array
N = raw_input()

# Elements in the array
arr_input = raw_input()
arr = [int(s) for s in arr_input.split(" ")]

M = raw_input()
for i in range(0, int(M)):
	X = raw_input()
	arr = [ele-1 if ele>int(X) else ele for ele in arr ]

print " ".join(map(str, arr))
