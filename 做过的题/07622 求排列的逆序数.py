import bisect
n=int(input())
a=[int(s) for s in input().split()]
l=[]
ans=0
for i in range(n):
    x=bisect.bisect_left(l,a[i])
    ans+=i-x
    l.insert(x,a[i])
print(ans)