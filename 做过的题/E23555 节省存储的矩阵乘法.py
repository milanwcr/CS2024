n,m1,m2=map(int,input().split())
a=[[0]*n for i in range(n)]
b=[[0]*n for i in range(n)]
for i in range(m1):
    x,y,aa=map(int,input().split())
    a[x][y]=aa
for i in range(m2):
    x,y,bb=map(int,input().split())
    b[x][y]=bb
c=[[0]*n for i in range(n)]
ans=[]
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j]+=a[i][k]*b[k][j]
        if c[i][j]!=0:
            ans.append([i,j,c[i][j]])
for i in ans:
    print(' '.join(map(str,i)))