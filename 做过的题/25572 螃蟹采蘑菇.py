from collections import deque
def bfs(x,y):
    queue=deque([(x,y)])
    while queue:
        x,y=queue.popleft()
        if (a[x][y]==9 and a[x+X][y+Y]!=1) or (a[x+X][y+Y]==9 and a[x][y]!=1):
            return 'yes'
        for j in range(4):
            nx,ny=x+dx[j],y+dy[j]
            if 0<=nx<n and 0<=ny<n and 0<=nx+X<n and 0<=ny+Y<n:
                if l[nx][ny] and a[nx][ny]!=1 and a[nx+X][ny+Y]!=1:
                    l[nx][ny]=False
                    queue.append((nx,ny))
    return 'no'

n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
l=[[True]*n for i in range(n)]
dx,dy=[1,0,-1,0],[0,1,0,-1]
for i in range(n):
    if 5 in a[i]:
        x,y=i,a[i].index(5)
        for j in range(4):
            if 0<=x+dx[j]<n and 0<=y+dy[j]<n and a[x+dx[j]][y+dy[j]]==5:
                X,Y=dx[j],dy[j]
                break
        l[x][y]=False
        print(bfs(x,y))
        break