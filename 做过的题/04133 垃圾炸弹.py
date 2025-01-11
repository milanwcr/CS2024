d=int(input())
l=[[0 for i in range(1025)] for j in range(1025)]
ll=[[0 for i in range(1026)] for j in range(1026)]
w=[]
n=int(input())
for i in range(n):
    x,y,g=map(int,input().split())
    w.append([x,y])
    l[x][y]=g
ll[1][1]=l[0][0]
for i in range(1,1025):
    ll[1][i+1]=ll[1][i]+l[0][i]
for i in range(1,1025):
    a=0
    for j in range(0,1025):
        a+=l[i][j]
        ll[i+1][j+1]=ll[i][j+1]+a
sm,ss=0,0
for i in range(n):
    for j in range(max(0,w[i][0]-d),min(w[i][0]+d,1024)+1):
        for k in range(max(0,w[i][1]-d),min(w[i][1]+d,1024)+1):
            s=ll[min(j+d,1024)+1][min(k+d,1024)+1]-ll[min(j+d,1024)+1][max(0,k-d)]-ll[max(0,j-d)][min(k+d,1024)+1]+ll[max(0,j-d)][max(0,k-d)]
            if sm<s:
                sm=s
                ss=1    
                sett=set()
                sett.add((j,k))
            elif sm==s and (j,k) not in sett:
                ss+=1
                sett.add((j,k))
print(ss,sm)