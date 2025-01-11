t,n=map(int,input().split())
dp=[0]*(t+1)
for i in range(n):
    ti,w=map(int,input().split())
    for j in range(t,ti,-1):
        if dp[j-ti]!=0:
            dp[j]=max(dp[j],dp[j-ti]+w)
    dp[ti]=max(w,dp[ti])
if dp[t]==0:
    print(-1)
else:
    print(dp[t])