t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=input().split()
    a=[int(s) for s in a]
    b=input().split()
    b=[int(s) for s in b]
    c=[(j,a[j]) for j in range(n)]
    a=sorted(c,key=lambda d : d[1])
    b.sort()
    ans=[0 for j in range(n)]
    for j in range(n):
        ans[a[j][0]]=str(b[j])
    print(' '.join(ans))