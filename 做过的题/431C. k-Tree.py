n,k,d=map(int,input().split())
dp=[0]*(n+1)
dp[0]=1
ddp=[0]*(n+1)
ddp[0]=1
for i in range(1,n+1):
    for j in range(1,min(k+1,i+1)):
        if j<d:
            ddp[i]+=ddp[i-j]
        dp[i]+=dp[i-j]
print((dp[n]-ddp[n])%1000000007)