n=int(input())
a=[int(s) for s in input().split()]
a.sort()
ans=0
i=0
while i<=n-1:
    j=1
    while i+j<=n-1:
        if a[i]==a[i+j]:
            j+=1
        else:
            break
    ans=max(ans,j)
    i+=j
print(ans)