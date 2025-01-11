m,n,p,q=map(int,input().split())
a,b=[],[]
ans=[[0 for i in range(n+1-q)] for j in range(m+1-p)]
for i in range(m):
    a.append([int(s) for s in input().split()])
for i in range(p):
    b.append([int(s) for s in input().split()])
for i in range(m+1-p):
    for j in range(n+1-q):
        for k in range(p):
            for l in range(q):
                ans[i][j]+=a[i+k][j+l]*b[k][l]
for i in range(m+1-p):
    print(' '.join(map(str,ans[i])))