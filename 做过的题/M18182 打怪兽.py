for _ in range(int(input())):
    n,m,b=map(int,input().split())
    a=[]
    for i in range(n):
        t,x=map(int,input().split())
        a.append([t,x])
    a.sort(key=lambda s:(s[0],-s[1]))
    i=0
    while i<n:
        t=a[i][0]
        f=0
        while i+f<n and f<m and a[i+f][0]==t:
            b-=a[i+f][1]
            f+=1
        i+=f
        while i<n and a[i][0]==t:
            i+=1
        if b<=0:
            print(t)
            break
    if b>0:
        print('alive')