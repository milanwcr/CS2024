s=input()
ans=0
ll=1
for i in range(len(s)-1):
    if int(s[i])+int(s[i+1])==1:
        ll+=1
    else:
        ans=max(ll,ans)
        ll=1
print(max(ans,ll))