for i in range(int(input())):
    n,x=map(int,input().split())
    a=[int(s) for s in input().split()]
    sum,d=0,100001
    for j in range(n):
        sum+=a[j]
        if a[j]%x!=0:
            d=min(d,j+1,n-j)
    if sum%x!=0:
        print(n)
    elif d==100001:
        print(-1)
    else:
        print(n-d)