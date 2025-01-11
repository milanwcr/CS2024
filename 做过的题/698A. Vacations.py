n=int(input())
a=[int(s) for s in input().split()]
dp=[[0,0,0] for i in range(n+1)]
for i in range(n):
    if a[i]==1:
        dp[i+1][1]=min(dp[i][0],dp[i][2])
        dp[i+1][2]=min(dp[i][0],dp[i][1],dp[i][2])+1
    if a[i]==2:
        dp[i+1][2]=min(dp[i][0],dp[i][1])
        dp[i+1][1]=min(dp[i][0],dp[i][1],dp[i][2])+1
    if a[i]==3:
        dp[i+1][1]=min(dp[i][0],dp[i][2])
        dp[i+1][2]=min(dp[i][0],dp[i][1])
    if a[i]==0:
        dp[i+1][2]=min(dp[i][0],dp[i][1],dp[i][2])+1
        dp[i+1][1]=min(dp[i][0],dp[i][1],dp[i][2])+1
    dp[i+1][0]=min(dp[i][0],dp[i][1],dp[i][2])+1
print(min(dp[n][1],dp[n][2],dp[n][0]))