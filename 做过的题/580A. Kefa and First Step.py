n=int(input())
l=[int(s) for s in input().split()]
l.append(0)
ans=0
left=0
while left<len(l)-1:
    le=1
    while l[left]<=l[left+1]:
        le+=1
        left+=1
    ans=max(ans,le)
    left+=1
print(ans)