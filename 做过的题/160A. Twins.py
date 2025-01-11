n=int(input())
a=[int(s) for s in input().split()]
s=sum(a)
ss=0
ans=0
a.sort(reverse=True)
while ss<=s-ss and ans<n:
    ss+=a[ans]
    ans+=1
print(ans)