def find(x):
    old,count=0,0
    for i in range(n+1):
        if d[i]-old<x:
            count+=1
        else:
            old=d[i]
    return count

l,n,m=map(int,input().split())
d=[int(input()) for i in range(n)]
d.append(l)
left,right=0,l//(n-m)+1
while left<right:
    mid=(left+right)//2
    if find(mid)>m:
        right=mid
    else:
        ans=mid
        left=mid+1
print(ans)