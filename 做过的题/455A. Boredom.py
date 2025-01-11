n=int(input())
a=[int(s) for s in input().split()]
l=[0]*(max(a)+1)
dp=[0]*(max(a)+2)
for i in a:
    l[i]+=i
for i in range(2,max(a)+2):
    dp[i]=max(dp[i-2]+l[i-2],dp[i-1])
print(max(dp[max(a)+1],dp[max(a)]+l[-1]))