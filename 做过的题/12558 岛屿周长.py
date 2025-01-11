n,m=map(int,input().split())
a=[]
c=[[0]*(m+2) for i in range(n+2)]
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(m):
        if a[i][j]==1:
            c[i+1][j]+=1
            c[i][j+1]+=1
            c[i+1][j+2]+=1
            c[i+2][j+1]+=1
ans=0
for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            ans+=4-c[i+1][j+1]
print(ans)