n,m=map(int,input().split())
a=[int(s) for s in input().split()]
b=[int(s) for s in input().split()]
c=[]
ap,bp=0,0
a.append(1000001)
b.append(1000001)
while ap<=n-1 or bp<=m-1:
    if a[ap]<b[bp]:
        c.append(a[ap])
        ap+=1
    else:
        c.append(b[bp])
        bp+=1
print(' '.join(map(str,c)))