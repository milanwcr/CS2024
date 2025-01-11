from collections import deque
def bfs(x,y):
    queue=deque([(x,y,0)])
    while queue:
        x,y,t=queue.popleft()
        for j in range(4):
            nx,ny=x+dx[j],y+dy[j]
            if 0<=nx<r and 0<=ny<c:
                if find[nx][ny][(t+1)%k]:
                    continue
                if a[nx][ny]=='E':
                    return t+1
                if a[nx][ny]!='#' or (t+1)%k==0:
                    find[nx][ny][(t+1)%k]=True
                    queue.append((nx,ny,t+1))
    return 'Oop!'
                    

dx,dy=[0,1,0,-1],[1,0,-1,0]
for _ in range(int(input())):
    r,c,k=map(int,input().split())
    a=[list(input()) for i in range(r)]
    find=[[[False for l in range(k)] for j in range(c)] for i in range(r)]
    for i in range(r):
        if 'S' in a[i]:
            find[i][a[i].index('S')][0]=True
            print(bfs(i,a[i].index('S')))
            break