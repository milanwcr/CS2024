def find(lis):
    global ans
    dp=[0]*n
    dp[0]=lis[0]
    for k in range(1,n):
        dp[k]=max(dp[k-1]+lis[k],lis[k])
        ans=max(ans,dp[k])
n=int(input())
a=[]
while len(a)<n*n:
    a.extend(input().split())
matrix=[list(map(int,a[i:i+n])) for i in range(0,n*n,n)]
summ=[[0]*n]
l=[0]*n
for i in range(n):
    for j in range(n):
        l[j]+=matrix[i][j]
    summ.append(l[:])
ans=float('-inf')
for i in range(n):
    for j in range(i+1,n+1):
        find([summ[j][k]-summ[i][k] for k in range(n)])
print(ans)