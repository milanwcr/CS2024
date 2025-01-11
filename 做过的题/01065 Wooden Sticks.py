from bisect import bisect_left
for _ in range(int(input())):
    n=int(input())
    lw=[int(s) for s in input().split()]
    l=[(lw[i],lw[i+1]) for i in range(0,2*n,2)]
    l.sort()
    w=[l[n-1-i][1] for i in range(n)]
    ww=[]
    for i in range(n):
        p=bisect_left(ww,w[i])
        if p<len(ww):
            ww[p]=w[i]
        else:
            ww.append(w[i])
    print(len(ww))