n=int(input())
a=0
for i in range(n):
    m=0
    l=[int(s) for s in input().split()]
    for j in range(3):
        if l[j]==1:
            m+=1
    if m>=2:
        a+=1
print(a)