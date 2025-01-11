n,m=map(int,input().split())
a=[[0 for i in range(m+2)] for j in range(n+2)]
ans=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    l=[int(s) for s in input().split()]
    for j in range(m):
        a[i+1][j+1]=l[j]
        ans[i][j]=l[j]
for i in range(1,n+1):
    for j in range(1,m+1):
        sum=a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i][j-1]+a[i+1][j-1]+a[i][j+1]+a[i+1][j+1]+a[i+1][j]
        if a[i][j]==0:
            if sum==3:
                ans[i-1][j-1]=1
        else:
            if sum!=2 and sum!=3:
                ans[i-1][j-1]=0
for i in range(n):
    print(' '.join(map(str,ans[i])))