import math
A, B = map(int, input().split())
if A % B == 0 or B % A == 0:
    print("Multiples")
else:
    print("No Multiples")
