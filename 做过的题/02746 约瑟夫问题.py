while True:
    n,m=map(int,input().split())
    if n==0:
        break
    l=[1 for i in range(n)]
    f=0
    i=1
    j=0
    while f<n-1:
        if l[j]==1:
            if i==m:
                f+=1
                l[j]=0
                i=1
            else:
                i+=1
        j=(j+1)%n
    print(l.index(1)+1)