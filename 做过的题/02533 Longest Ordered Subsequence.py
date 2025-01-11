n=int(input())
a=[int(s) for s in input().split()]
c=[0]*n
ans=0
for i in range(n):
    maxx=0
    for j in range(i):
        if a[i]>a[j]:
            maxx=max(maxx,c[j])
    c[i]=maxx+1
    ans=max(ans,c[i])
print(ans)