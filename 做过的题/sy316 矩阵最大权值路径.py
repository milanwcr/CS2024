def find(x,y,s,length):
    global ans,l
    if x==n-1 and y==m-1 and ans<length:
        ans=length
        l=s[:]
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and (nx,ny) not in s:
            ss=s[:]
            ss.append((nx,ny))
            find(nx,ny,ss,length+a[nx][ny])

n,m=map(int,input().split())
dx=[0,1,0,-1]
dy=[1,0,-1,0]
a=[list(map(int,input().split())) for i in range(n)]
l=[]
ans=float('-inf')
find(0,0,[(0,0)],a[0][0])
for i in range(len(l)):
    print(str(l[i][0]+1)+' '+str(l[i][1]+1))