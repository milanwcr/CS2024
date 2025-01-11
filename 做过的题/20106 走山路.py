from heapq import heappush,heappop
def bfs(x,y):
    global m,n,dx,dy,a,ans,x2,y2
    heap=[(0,x,y)]
    s=set()
    while heap:
        h,x,y=heappop(heap)
        if (x,y) in s:
            continue
        s.add((x,y))
        if x==x2 and y==y2:
            return h
        for j in range(4):
            nx,ny=x+dx[j],y+dy[j]
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in s and a[nx][ny]!='#':
                heappush(heap,(h+abs(int(a[x][y])-int(a[nx][ny])),nx,ny))
    return 'NO'

dx,dy=[0,1,0,-1],[1,0,-1,0]
m,n,p=map(int,input().split())
a=[list(input().split()) for i in range(m)]
for i in range(p):
    x1,y1,x2,y2=map(int,input().split())
    if a[x1][y1]=='#' or a[x2][y2]=='#':
        print('NO')
        continue
    print(bfs(x1,y1))