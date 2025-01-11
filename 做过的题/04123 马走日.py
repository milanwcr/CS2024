def find(i,j,depth,s):
    for k in range(8):
        ni=i+dx[k]
        nj=j+dy[k]
        if 0<=ni<n and 0<=nj<m and (ni,nj) not in s:
            l=list(s)
            ll=l[:]
            ll.append((ni,nj))
            find(ni,nj,depth+1,set(ll))
    if depth==n*m:
        ans[0]+=1

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[-2,-1,1,2,2,1,-1,-2]
for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    ans=[0]
    find(x,y,1,set([(x,y)]))
    print(ans[0])