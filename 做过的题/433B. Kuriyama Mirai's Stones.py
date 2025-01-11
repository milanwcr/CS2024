n=int(input())
v=[int(s) for s in input().split()]
u=sorted(v)
uv=[[0,0] for s in range(n+1)]
for i in range(1,n+1):
    uv[i][0]=uv[i-1][0]+v[i-1]
    uv[i][1]=uv[i-1][1]+u[i-1]
m=int(input())
for i in range(m):
    ty,l,r=map(int,input().split())
    print(uv[r][ty-1]-uv[l-1][ty-1])