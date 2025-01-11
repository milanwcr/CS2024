n,q=map(int,input().split())
l=set()
f=0
for i in range(q):
    x,y=map(int,input().split())
    l.add((x,y))
    for j in range(1,n+1):
        if (y,j) in l and (j,x) in l:
            f=1
            break
if f==0:
    print("No")
else:
    print("Yes")