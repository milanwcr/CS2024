n=int(input())
a=[]
for i in range(n):
    s,f=map(int,input().split())
    a.append([s,f])
a.sort()
i=0
ans=0
while i<n:
    ans+=1
    right=a[i][1]
    while i<n and a[i][0]<=right:
        right=min(right,a[i][1])
        i+=1
print(ans)