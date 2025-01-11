n=int(input())
l=[0]*n
f=[]
s=[int(a) for a in input().split()]
for i in range(len(s)):
    if s[i]<=n:
        l[s[i]-1]=1
    else:
        f.append(s[i])
f.sort()
for i in range(n):
    if l[i]==0:
        print(i+1,end=' ')
print()
for i in f:
    print(i,end=' ')