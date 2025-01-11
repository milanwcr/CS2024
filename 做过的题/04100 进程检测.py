m=int(input())
for i in range(m):
    n=int(input())
    a=[]
    for j in range(n):
        s,d=map(int,input().split())
        a.append([s,d])
    a.sort()
    ans,k=0,0
    while k<=n-1:
        ans+=1
        minx=a[k][1]
        while k<=n-1 and a[k][0]<=minx:
            minx=min(minx,a[k][1])
            k+=1
    print(ans)