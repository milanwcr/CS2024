from collections import deque
def findisland(x,y,depth):
    l[x][y]=2
    queue=deque([(x,y,depth)])
    while queue:
        x,y,depth=queue.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and l[nx][ny]==1 and depth!=0:
                return depth
            if 0<=nx<n and 0<=ny<m and l[nx][ny]==1 and depth==0:
                queue.appendleft((nx,ny,0))
                l[nx][ny]=2
                continue
            if 0<=nx<n and 0<=ny<m and l[nx][ny]==0:
                queue.append((nx,ny,depth+1))
                l[nx][ny]=2

n=int(input())
a=[[int(s) for s in input()] for i in range(n)]
m=len(a[0])
dx,dy=[0,1,0,-1],[1,0,-1,0]
l=[a[i][:] for i in range(n)]
j=0
for i in range(n):
    if 1 in l[i]:
        print(findisland(i,l[i].index(1),0))
        break