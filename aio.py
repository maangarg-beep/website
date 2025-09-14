import math
k, n = map(int, input().split())

if k<= n:
    print("0")
else: 
    h = k - n
    p = n + 1
    print(math.ceil(h / p))
