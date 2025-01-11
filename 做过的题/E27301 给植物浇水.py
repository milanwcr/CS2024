n,a,b=map(int,input().split())
l,r,ans=0,n-1,0
left,right=a,b
w=list(map(int,input().split()))
while l<r:
    if left<w[l]:
        left=a
        ans+=1
    if right<w[r]:
        right=b
        ans+=1
    left-=w[l]
    right-=w[r]
    l+=1
    r-=1
if l==r and w[l]>max(left,right):
    ans+=1
print(ans)