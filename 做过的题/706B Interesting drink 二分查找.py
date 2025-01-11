def bs(a,q):
    if q>=a[n-1]:
        return n
    left=0
    right=n-1
    while left<=right:
        mid=left+(right-left)//2
        if a[mid]<=q and a[mid+1]>q:
            return mid+1
        elif a[mid]>q:
            right=mid-1
        else:
            left=mid+1
    return 0

n=int(input())
x=[int(s) for s in input().split()]
x.sort()
for i in range(int(input())):
    m=int(input())
    print(bs(x,m))