n=int(input())
l=[[0,0] for i in range(n)]
for i in range(n):
    l[i][0],l[i][1]=map(int,input().split())
l.sort()
f=False
for i in range(n-1):
    if l[i][1]>l[i+1][1]:
        f=True
        break
if f:
    print("Happy Alex")
else:
    print("Poor Alex")