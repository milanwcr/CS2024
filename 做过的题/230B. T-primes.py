from math import sqrt
n=int(input())
l=[int(s) for s in input().split()]
s=set()
a=[1 for i in range(1000000)]
a[0]=0
a[1]=0
for i in range(2,1000000):
    if a[i]==1:
        s.add(i)
        for j in range(i,1000000,i):
            a[j]=0
for i in l:
    if int(sqrt(i)) in s and int(sqrt(i))**2==i:
        print("YES")
    else:
        print("NO")