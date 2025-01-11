n,p=map(int,input().split())
l=set()
f=0
for i in range(p):
    x,y=map(int,input().split())
    l.add((x,y))
    if (y,x) in l:
        f=1
if f==0:
    print("No")
else:
    print("Yes")