n,m=map(int,input().split())
a=[int(s) for s in input().split()]
dp=[0]+[10000000]*(2*m)
for i in range(1,m+1):
    c=float('inf')
    for j in range(n):
        c=min(c,dp[i-a[j]]+1)
    dp[i]=c
if dp[m]>1000000:
    print(-1)
else:
    print(dp[m])