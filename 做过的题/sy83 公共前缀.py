n=int(input())
l=[0 for i in range(n)]
le=51
m=0
ff=0
for i in range(n):
    l[i]=input()
    if le>len(l[i]):
        le=len(l[i])
        m=i
for i in range(len(l[m]),0,-1):
    f=0
    for j in range(n):
        if l[0][:i]!=l[j][:i]:
            f=1
            break
    if f==0:
        print(l[0][:i])
        ff=1
        break
if ff==0:
    print()