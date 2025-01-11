n=int(input())
a=[int(s) for s in input().split()]
dp=[[1,0] for i in range(n)]
ans=1
for i in range(1,n):
    for j in range(i):
        if dp[j][1]==0 and a[i]!=a[j]:
            dp[i][0]=2
            dp[i][1]=a[i]-a[j]
        elif dp[j][1]*(a[i]-a[j])<0:
            if dp[i][0]<dp[j][0]+1:
                dp[i][0]=dp[j][0]+1
                dp[i][1]=a[i]-a[j]
    ans=max(ans,dp[i][0])
print(ans)