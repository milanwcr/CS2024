n,m,k=map(int,input().split())
l=[[0 for i in range(m+2)] for j in range(n+2)]
f=0
for i in range(k):
    a,b=map(int,input().split())
    l[a][b]=1
    if f==0 and ((l[a-1][b-1]==1 and l[a][b-1]==1 and l[a-1][b]==1) or (l[a-1][b+1]==1 and l[a][b+1]==1 and l[a-1][b]==1) or(l[a+1][b-1]==1 and l[a][b-1]==1 and l[a+1][b]==1) or (l[a+1][b+1]==1 and l[a][b+1]==1 and l[a+1][b]==1)):
        print(i+1)
        f=1
if f==0:
    print(0)