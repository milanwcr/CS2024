case=0
while True:
    n,d=map(int,input().split())
    if n==0:
        break
    case+=1
    a=[]
    ym=0
    for i in range(n):
        x,y=map(int,input().split())
        ym=max(ym,y)
        a.append((x-(d**2-y**2)**(1/2),x+(d**2-y**2)**(1/2)))
    input()
    if ym>d:
        print(f'Case {case}: {-1}')
        continue
    a.sort(key=lambda s:s[0])
    i,ans=0,0
    while i<n:
        ans+=1
        j=i+1
        xm=a[i][1]
        while j<n and a[j][0]<=xm:
            xm=min(xm,a[j][1])
            j+=1
        i=j
    print(f'Case {case}: {ans}')