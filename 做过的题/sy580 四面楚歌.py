n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([int(s) for s in input().split()])
maxx=0
for i in range(n):
    for j in range(m):
        maxx=max(maxx,a[i][j]*(a[0][j]*1000+a[i][m-1]*100+a[n-1][j]*10+a[i][0]))
print(maxx)