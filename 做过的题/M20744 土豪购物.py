p=list(map(int,input().split(',')))
n,ans=len(p),p[0]
dp=[[0,0]]+[[p[i],p[i]] for i in range(n)]
for i in range(2,n+1):
    dp[i][0]=max(dp[i-1][0]+p[i-1],dp[i][0],dp[i-2][1]+p[i-1])
    dp[i][1]=max(dp[i][1],dp[i-1][1]+p[i-1])
    ans=max(dp[i][0],ans)
print(ans)