n,k=map(int,input().split())
a=[int(s) for s in input().split()]
l=0
r=n-1
ans=0
while l<r:
    if a[l]+a[r]==k:
        ans+=1
        l+=1
        r-=1
    elif a[l]+a[r]<=k:
        l+=1
    else:
        r-=1
print(ans)