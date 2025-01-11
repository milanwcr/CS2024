n=int(input())
a=[int(s) for s in input().split()]
m=int(input())
b=[int(s) for s in input().split()]
a.sort()
b.sort()
p1,p2,ans=0,0,0
while p1<=n-1 and p2<=m-1:
    if abs(a[p1]-b[p2])<=1:
        ans+=1
        p1+=1
        p2+=1
    elif a[p1]>b[p2]:
        p2+=1
    else:
        p1+=1
print(ans)