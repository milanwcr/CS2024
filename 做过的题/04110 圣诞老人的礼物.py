n,w=map(int ,input().split())
l=[[0,0] for i in range(n)]
for i in range(n):
    l[i][0],l[i][1]=map(int,input().split())
l.sort(key=lambda x:x[0]/x[1],reverse=True)
v=0
for i in range(n):
    if w>=l[i][1]:
        w-=l[i][1]
        v+=l[i][0]
    else:
        v+=l[i][0]*w/l[i][1]
        break
print('{:.1f}'.format(v))