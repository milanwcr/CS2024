t,k=map(int,input().split())
l=[]
n=0
for i in range(t):
    a,b=map(int,input().split())
    n=max(n,b)
    l.append((a,b))
dp=[1]*(n+1)
ans=[0]
for i in range(k,n+1):
    dp[i]=(dp[i-1]+dp[i-k])%1000000007
for i in range(1,n+1):
    ans.append((dp[i]+ans[i-1])%1000000007)
for a,b in l:
    print((1000000007+ans[b]-ans[a-1])%1000000007)