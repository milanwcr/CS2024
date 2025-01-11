l,m=input().split()
l=int(l)
m=int(m)
list=[['',''] for i in range(m)]
s=0
for i in range(m):
    list[i][0],list[i][1]=input().split()
    list[i][0]=int(list[i][0])
    list[i][1]=int(list[i][1])
c=sorted(list,key=lambda a:a[0])
for i in range(m):
    if i==0:
        s+=c[i][1]-c[i][0]+1
    else:
        if c[i][1]<=c[i-1][1]:
            c[i][1]=c[i-1][1]
            continue
        elif c[i][0]<=c[i-1][1]:
            s+=c[i][1]-c[i-1][1]
        else:
            s+=c[i][1]-c[i][0]+1
print(l-s+1)