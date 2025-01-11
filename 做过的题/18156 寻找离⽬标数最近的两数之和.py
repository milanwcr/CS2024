t=int(input())
a=[int(s) for s in input().split()]
a.sort()
left,right=0,len(a)-1
d,minn=1000000,1000000
while left<right:
    if d>abs(t-a[left]-a[right]):
        d=abs(t-a[left]-a[right])
        minn=a[left]+a[right]
    elif d==abs(t-a[left]-a[right]):
        minn=min(minn,a[left]+a[right])
    if a[left]+a[right]>=t:
        right-=1
    elif a[left]+a[right]<t:
        left+=1
print(minn)