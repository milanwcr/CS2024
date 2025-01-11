l=list(map(int,input().split()))
l.append(-1)
l.insert(0,float('inf'))
i,n=1,len(l)
ans,minn=0,float('inf')
while i<n-1:
    if l[i]<=l[i-1] and l[i]<l[i+1]:
        minn=min(minn,l[i])
    elif l[i]>l[i-1] and l[i]>=l[i+1]:
        ans=max(l[i]-minn,ans)
    i+=1
print(ans)