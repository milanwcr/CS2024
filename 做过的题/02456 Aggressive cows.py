def search(m):
    count=0
    old=x[0]
    for i in range(1,n):
        if x[i]-old>=m:
            count+=1
            old=x[i]
    return count
n,c=map(int,input().split())
x=[int(input()) for i in range(n)]
x.sort()
l,r=0,(x[-1]-x[0])//(c-1)
while l<=r:
    mid=(l+r)//2
    if search(mid)>=c-1:
        l=mid+1
    else:
        r=mid-1
print(r)