from collections import deque
def find():
    queue=deque([(0,0,0)])
    global ans
    while queue:
        x,y,depth=queue.popleft()
        if a[x][y]==1:
            ans=depth
            return
        for i in range(4):
            if 0<=x+dx[i]<m and 0<=y+dy[i]<n and vi[x+dx[i]][y+dy[i]]!=1 and a[x+dx[i]][y+dy[i]]!=2:
                queue.append((x+dx[i],y+dy[i],depth+1))
                vi[x+dx[i]][y+dy[i]]=1

m,n=map(int,input().split())
dx=[0,-1,0,1]
dy=[-1,0,1,0]
a=[list(map(int,input().split())) for i in range(m)]
vi=[[0]*n for i in range(m)]
ans=1000000
find()
if ans!=1000000:
    print(ans)
else:
    print('NO')