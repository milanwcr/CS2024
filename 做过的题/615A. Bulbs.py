n,m=map(int,input().split())
a=[0 for i in range(m)]
for i in range(n):
    l=input().split()
    for j in l[1:len(l)]:
        a[int(j)-1]=1
if 0 in a:
    print("NO")
else:
    print("YES")