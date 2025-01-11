n,t=map(int,input().split())
p=list(map(int,input().split()))
sp=sum(p)
dp=[[0]*(sp+1) for i in range(n+1)]
for i in range(n):
    for j in range(sp,0,-1):
        if j>=p[i]:
            dp[i+1][j]=max(dp[i][j],dp[i][j-p[i]]+p[i])
        else:
            dp[i+1][j]=dp[i][j]
if sp<t:
    print(0)
else:
    for i in range(t,sp+1):
        if dp[n][i]>=t:
            print(dp[n][i])
            break