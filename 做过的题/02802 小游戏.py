from collections import deque
def find(x1,y1,x2,y2):
    queue=deque([(x1,y1,0)])
    while queue:
        x,y,depth=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            while 0<=nx<=w+1 and 0<=ny<=h+1 and l[ny][nx]:
                if nx==x2 and ny==y2:
                    return depth+1
                l[ny][nx]=False
                queue.append((nx,ny,depth+1))
                nx+=dx[i]
                ny+=dy[i]
    return -1

dx=[0,1,0,-1]
dy=[1,0,-1,0]
m=0
while True:
    m+=1
    w,h=map(int,input().split())
    if w==0:
        break
    print(f'Board #{m}:')
    a=[list(input()) for i in range(h)]
    n=0
    while True:
        n+=1
        x1,y1,x2,y2=map(int,input().split())
        if x1==0:
            break
        l=[[True]*(w+2) for i in range(h+2)]
        for i in range(h):
            for j in range(w):
                if a[i][j]=='X':
                    l[i+1][j+1]=False
        l[y2][x2]=True
        ans=find(x1,y1,x2,y2)
        if ans==-1:
            print(f'Pair {n}: impossible.')
        else:
            print(f'Pair {n}: {ans} segments.')
    print()