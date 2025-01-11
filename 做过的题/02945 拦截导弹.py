k=int(input())
a=[int(s) for s in input().split()]
maxx=[1 for i in range(k)]
maxxx=1
for i in range(1,k):
    for j in range(0,i):
        if a[j]>=a[i]:
            maxx[i]=max(maxx[i],1+maxx[j])
            maxxx=max(maxxx,maxx[i])
print(maxxx)