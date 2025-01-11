n=int(input())
l=[int(s) for s in input().split()]
f=0
for i in range(0,n-1):
    if l[i]>l[i+1]:
        f=1
        print('NO')
        break
if f==0:
    print('YES')