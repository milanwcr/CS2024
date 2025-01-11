m=int(input())
for i in range(m):
    l,n=map(int,input().split())
    d=[int(s) for s in input().split()]
    maxx=0
    minn=l/2
    for j in d:
        maxx=max(maxx,j,l-j)
        minn=min(minn,abs(j-l/2))
    print(f'{int(l/2-minn)} {maxx}')