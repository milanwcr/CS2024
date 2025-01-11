import sys
sys.setrecursionlimit(1000000000)
def find(x,y):
    global f
    for k in range(8):
        if 0<=x+d[k][0]<n and 0<=y+d[k][1]<m and s[x+d[k][0]][y+d[k][1]]==1:
            f+=1
            s[x+d[k][0]][y+d[k][1]]=0
            find(x+d[k][0],y+d[k][1])
d=[(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1),(-1,1),(1,-1)]
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[]
    s=[[0]*m for i in range(n)]
    ans=0
    for i in range(n):
        a.append(input())
        for j in range(m):
            if a[i][j]=='W':
                s[i][j]=1
    for i in range(n):
        for j in range(m):
            if s[i][j]==1:
                f=1
                s[i][j]=0
                find(i,j)
                ans=max(ans,f)
    print(ans)