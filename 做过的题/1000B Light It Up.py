n,m=map(int,input().split())
a=[int(s) for s in input().split()]
a.insert(0,0)
a.append(m)
s=[0 for i in range(n+1)]
su=0
for i in range(n,-1,-1):
    if i%2==0:
        su+=a[i+1]-a[i]
    else:
        s[i]=su
ans=0
for i in range(1,n+1,2):
    if a[i]-a[i-1]>1 or a[i+1]-a[i]>1:
        ans=max(ans,m-2*s[i]-1-a[i])
print(ans+su)