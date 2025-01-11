n,d=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
ans=[]
while len(l)>=1:
    minn,maxx=l[0],l[0]
    a=[l[0]]
    del l[0]
    j=0
    while j<len(l):
        if maxx<=l[j]+d and minn>=l[j]-d:
            maxx=max(maxx,l[j])
            minn=min(minn,l[j])
            a.append(l[j])
            del l[j]
        else:
            maxx=max(maxx,l[j])
            minn=min(minn,l[j])
            j+=1
    a.sort()
    ans+=a
for i in range(n):
    print(ans[i])