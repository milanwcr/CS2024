n=int(input())
l=[int(a) for a in input().split()]
for i in range(n):
    if l[i]%2==0:
        l[i]=0
    else:
        l[i]=1
s=[[l[i],i] for i in range(n)]
s.sort()
if s[1][0]==0:
    print(s[n-1][1]+1)
else:
    print(s[0][1]+1)