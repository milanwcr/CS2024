n=int(input())
x=[int(s) for s in input().split()]
x.sort()
a=[0 for i in range(100000)]
j=0
for i in range(100000):
    while j<n and x[j]==i+1:
        j+=1
    a[i]=j
q=int(input())
for i in range(q):
    m=int(input())
    if m>100000:
        print(n)
    else:
        print(a[m-1])