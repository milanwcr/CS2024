n,m=map(int,input().split())
dp=[1,1]+[0]*(m-2)
for i in range(n-1):
    s=sum(dp)
    for j in range(1,m):
        dp[m-j]=dp[m-j-1]
    dp[0]=s
print(sum(dp))