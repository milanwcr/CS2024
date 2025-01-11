def dfs(x,y):
    dx,dy=[0,1,0,-1],[1,0,-1,0]
    if dp[x][y]!=1:
        return dp[x][y]
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and h[nx][ny]>h[x][y]:
            dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]


r,c=map(int,input().split())
h=[list(map(int,input().split())) for i in range(r)]
dp=[[1]*c for i in range(r)]
ans=0
for i in range(r):
    for j in range(c):
        ans=max(ans,dfs(i,j))
print(ans)