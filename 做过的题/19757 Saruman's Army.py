while True:
    r,n=map(int,input().split())
    if r==-1:
        break
    x=[int(s) for s in input().split()]
    x.sort()
    i,ans=0,0
    while i<=n-1:
        j,k=0,0
#        if i+1<=n-1 and x[1+i]<=x[i]+r:
        while i+j<n-1:
            if x[j+i]<=x[i]+r and x[j+i+1]>x[i]+r:
                break
            j+=1
        while i+j+k<n-1 :
            if x[j+i+k]<=x[i+j]+r and x[j+i+k+1]>x[i+j]+r:
                break
            k+=1
        ans+=1
        i+=j+k+1
    print(ans)