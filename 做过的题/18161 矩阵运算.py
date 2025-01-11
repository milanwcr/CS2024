r1,c1=map(int,input().split())
a=[[0]*c1 for _ in range(r1)]
for i in range(r1):
    l=input().split()
    for j in range(c1):
        a[i][j]=int(l[j])
r2,c2=map(int,input().split())
b=[[0]*c2 for _ in range(r2)]
for i in range(r2):
    l=input().split()
    for j in range(c2):
        b[i][j]=int(l[j])
r3,c3=map(int,input().split())
c=[[0]*c3 for _ in range(r3)]
for i in range(r3):
    l=input().split()
    for j in range(c3):
        c[i][j]=int(l[j])
if c1!=r2 or r1!=r3 or c2!=c3:
    print('Error!')
else:
    for i in range(r1):
        for j in range(c2):
            s=0
            for k in range(c1):
                s+=a[i][k]*b[k][j]
            s+=c[i][j]
            if j==c2-1:
                print(s)
            else:
                print(s,end=' ')