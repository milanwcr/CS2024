n,k=map(int,input().split())
l=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
ans=[]
while n>=k:
    ans.append(l[n%k])
    n=n//k
if n!=0:
    ans.append(l[n])
ans.reverse()
print(''.join(ans))