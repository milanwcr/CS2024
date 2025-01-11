s=input()
n=len(s)
a=[]
i=1
while i<=n:
    a.append(s[i-1])
    i*=2
l,r=0,len(a)-1
ans=[]
while l<r:
    ans.append(a[l])
    ans.append(a[r])
    l+=1
    r-=1
if l==r:
    ans.append(a[l])
print(''.join(ans))