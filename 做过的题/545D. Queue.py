n=int(input())
t=[int(s) for s in input().split()]
t.sort()
tt,ans=0,0
for i in t:
    if i>=tt:
        ans+=1
        tt+=i
print(ans)