n=int(input())
l=[int(s) for s in input().split()]
k=int(input())
l.sort()
left=0
right=n-1
ans=0
while left<right:
    if l[left]+l[right]==k:
        ans+=1
        left+=1
        right-=1
    elif l[left]+l[right]>k:
        right-=1
    else:
        left+=1
print(ans)