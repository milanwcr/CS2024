from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))
ans,s,fu=0,0,[]
for i in range(n):
    if a[i]>=0:
        ans+=1
        s+=a[i]
    elif a[i]+s>=0:
        ans+=1
        s+=a[i]
        fu.insert(bisect_left(fu,a[i]),a[i])
    else:
        x=bisect_left(fu,a[i])
        if x!=0:
            s+=a[i]-fu[0]
            fu.insert(x,a[i])
            del fu[0]
print(ans)