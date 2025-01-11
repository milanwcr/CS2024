n,a,b,c=map(int,input().split())
ans=[0]*10000
ans[a],ans[b],ans[c]=1,1,1
for i in range(1,n+1):
    if ans[i-a]!=0 or ans[i-b]!=0 or ans[i-c]!=0:
        ans[i]=max(ans[i-a],ans[i-b],ans[i-c])+1
print(ans[n])