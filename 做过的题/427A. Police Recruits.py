n=int(input())
l=[int(s) for s in input().split()]
ans=0
p=0
for i in l:
    if i==-1 and p==0:
        ans+=1
    if i!=-1:
        p+=i
    if i==-1 and p!=0:
        p-=1
print(ans)