from functools import cmp_to_key
def custom_cmp_max(x, y):
    if x + y > y + x:
        return 1
    elif x + y < y + x:
        return -1
    return 0
m=int(input())
n=int(input())
a=list(input().split())
a.sort(key=cmp_to_key(custom_cmp_max))
dp=[[0]*(m+1) for i in range(n)]
for i in range(n):
    l=len(a[i])
    for j in range(1,m+1):
        if l==j:
            dp[i][j]=int(a[i])
        if l<j and dp[i-1][j-l]!=0:
            dp[i][j]=max(int(str(dp[i-1][j-l])+a[i]),int(a[i]+str(dp[i-1][j-l])))
        dp[i][j]=max(dp[i][j],dp[i-1][j])
print(dp[n-1][m])