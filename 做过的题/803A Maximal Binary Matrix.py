n,k=map(int,input().split())
if k>n**2:
    print(-1)
else:
    a=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i,n):
            if k>0:
                if j==i:
                    a[i][j]=1
                    k-=1
                elif k==1:
                    a[i+1][i+1]=1
                    k-=1
                else:
                    a[i][j],a[j][i]=1,1
                    k-=2
    for i in range(n):
        print(' '.join(map(str,a[i])))