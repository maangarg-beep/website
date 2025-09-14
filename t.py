import sys
sys.setrecursionlimit(1000000000)

n, l = map(int, input().split())
o = []
p = []
h = -1





clue = [0] * (l+1)
for i in range(n):
    a, b = map(int, input().split())
    o.append(a)
    p.append(b)
    h+=1
    for t in range(o[h], p[h] + 1):
        clue[t] += 1

d = clue.count(n)


print(d)



 
  