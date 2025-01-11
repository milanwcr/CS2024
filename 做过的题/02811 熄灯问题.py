def bottom(x,y):
    for k in range(5):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<5 and 0<=ny<6:
            acopy[nx][ny]=1-acopy[nx][ny]

dx,dy=[0,1,0,-1,0],[1,0,-1,0,0]
a=[list(map(int,input().split())) for i in range(5)]
for i in range(64):
    acopy=[a[j][:] for j in range(5)]
    ans=[list(format(i,'b').zfill(6))]
    for j in range(6):
        if ans[0][j]=='1':
            bottom(0,j)
    for j in range(4):
        ans.append([])
        for k in range(6):
            if acopy[j][k]==1:
                bottom(j+1,k)
                ans[-1].append('1')
            else:
                ans[-1].append('0')
    if 1 not in acopy[-1]:
        for j in range(5):
            print(' '.join(ans[j]))
        break