ans3=[0]
for i in range(12):
    ans3.append(2*ans3[i]+1)
ans=[0,1]
print(1)
for n in range(2,13):
    minn=float('inf')
    for i in range(1,n+1):
        minn=min(minn,ans3[i]+2*ans[n-i])
    ans.append(minn)
    print(minn)