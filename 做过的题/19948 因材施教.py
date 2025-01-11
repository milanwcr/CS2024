n,m=map(int,input().split())
l=[int(s) for s in input().split()]
l.sort()
d=[]
for i in range(n-1):
    d.append(l[i+1]-l[i])
d.sort()
print(l[-1]-l[0]-sum(d[-m+1:]))