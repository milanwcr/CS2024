n,b=map(int,input().split())
price=[int(s) for s in input().split()]
weight=[int(s) for s in input().split()]
ans=[0]*(b+1)
a=[[-1] for s in range(b+1)]
for i in range(n):
    ans[weight[i]]=price[i]
    a[weight[i]].append(i)
for i in range(1,b+1):
    maxx,flag=0,-1
    for j in range(n):
        if i>=weight[j] and ans[i-weight[j]]!=0:
            if j not in a[i-weight[j]]:
                if maxx<ans[i-weight[j]]+price[j]:
                    maxx=ans[i-weight[j]]+price[j]
                    flag=j
    if flag==-1 and ans[i]==0:
        ans[i]=ans[i-1]
    else:
        a[i]=a[i-weight[flag]]+[flag]
        ans[i]=ans[i-weight[flag]]+price[flag]    
print(ans[b])