n,m=map(int,input().split())
a=[int(s) for s in input().split()]
ans=[0]*n
ans[-1]=1
sett={a[-1]}
for i in range(n-2,-1,-1):
    if a[i] in sett:
        ans[i]=ans[i+1]
    else:
        ans[i]=ans[i+1]+1
        sett.add(a[i])
for i in range(m):
    print(ans[int(input())-1])