def put(start,s,num):
    for i in range(s-1):
        a[start][start+i]=num+i
    for i in range(s-1):
        a[start+i][start+s-1]=num+s-1+i
    for i in range(s-1):
        a[start+s-1][start+s-1-i]=num+2*s-2+i
    for i in range(s-1):
        a[start+s-1-i][start]=num+3*s-3+i
    if s==1:
        a[start][start]=num
        return
    if s==2:
        return
    put(start+1,s-2,num+4*s-4)

n=int(input())
a=[[0]*(n) for i in range(n)]
put(0,n,1)
for i in range(n):
    print(' '.join(map(str,a[i])))