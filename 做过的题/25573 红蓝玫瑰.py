s=list(input())
n=len(s)
dp1=[0]*(n+1)
dp2=[0]*(n+1)
for i in range(n):
    if s[i]=='R':
        dp1[i+1]=min(dp1[i],dp2[i]+1)
        dp2[i+1]=min(dp1[i]+1,dp2[i]+1)
    if s[i]=='B':
        dp2[i+1]=min(dp2[i],dp1[i]+1)
        dp1[i+1]=min(dp2[i]+1,dp1[i]+1)
print(min(dp1[n],dp2[n]+1))