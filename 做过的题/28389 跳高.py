from bisect import bisect_left
n=int(input())
h=[int(s) for s in input().split()]
l=[]
h.reverse()
for i in range(n):
    p=bisect_left(l,h[i])
    if p<len(l):
        l[p]=h[i]
    else:
        l.append(h[i])
print(len(l))