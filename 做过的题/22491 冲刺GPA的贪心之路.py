h=int(input())
m=int(input())
h=h*2-m*0.5
l=[]
for i in range(m):
    s,c=map(float,input().split())
    l.append([s,c])
l.sort(key=lambda x:(x[0]*x[1],x[0]),reverse=True)
ans=0
for i in range(m):
    if h>5/l[i][0]:
        ans+=5*l[i][1]
        h-=5/l[i][0]
    else:
        ans+=h*l[i][0]*l[i][1]
        break
print('{:.1f}'.format(ans))