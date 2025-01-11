n=int(input())
l=[]
for i in range(n):
    x,h=map(int,input().split())
    l.append([x,h])
ans=2
for i in range(1,n-1):
    if l[i-1][0]<l[i][0]-l[i][1]:
        ans+=1
    elif l[i+1][0]>l[i][0]+l[i][1]:
        ans+=1
        l[i][0]+=l[i][1]
if n==1:
    print(1)
else:
    print(ans)