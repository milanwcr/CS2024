n,l=map(int,input().split())
a=[int(s) for s in input().split()]
a.sort()
d=0
for i in range(n-1):
    d=max(d,a[i+1]-a[i])
print("{:.10f}".format(max(d,a[0]*2,(l-a[-1])*2)/2))