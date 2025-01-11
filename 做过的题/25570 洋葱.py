n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(n//2):
    s=sum(a[i][i:n-i])+sum(a[n-1-i][i:n-i])
    for j in range(i+1,n-1-i):
        s+=a[j][i]+a[j][n-1-i]
    ans=max(ans,s)
print(max(ans,a[n//2][n//2]))