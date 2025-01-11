n=int(input())
a=[int(s) for s in input().split()]
for i in range(1,n):
    a[i]+=a[i-1]
c,ans=0,0
for i in range(n-1):
    if a[i]/2==a[-1]/3:
        ans+=c
    if a[i]==a[-1]/3:
        c+=1
print(ans)