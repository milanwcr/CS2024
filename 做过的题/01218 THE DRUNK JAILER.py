n=int(input())
for i in range(n):
    a=int(input())
    l=[0]*a
    for j in range(a):
        for k in range(a):
            if (k+1)%(j+1)==0:
                l[k]=1-l[k]
    ans=0
    for j in range(a):
        if l[j]==1:
            ans+=1
    print(ans)