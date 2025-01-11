n=int(input())
h1=[int(s) for s in input().split()]
h2=[int(s) for s in input().split()]
dp=[[0,0,0] for i in range(n+1)]
for i in range(n):
    dp[i+1][0]=max(dp[i][0],dp[i][1],dp[i][2])
    dp[i+1][1]=max(dp[i][0],dp[i][2])+h1[i]
    dp[i+1][2]=max(dp[i][0],dp[i][1])+h2[i]
print(max(dp[n][0],dp[n][1],dp[n][2]))