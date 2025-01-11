n,d=map(int,input().split())
l=[]
ll=[]
minn,maxx,kmin,kmax=2000000001,0,0,0
for i in range(n):
    l.append(int(input()))
    ll.append([l[i],i,maxx,kmax,minn,kmin])
    if minn>=l[i]:
        minn=l[i]
        kmin=i
    if maxx<=l[i]:
        maxx=l[i]
        kmax=i
ll.sort(key=lambda x:(-x[0],-x[1]))
print(ll)
for i in range(n):
    if ll[i][1]>0 and ll[i][2]>ll[i][0] and ll[i][2]<=ll[i][0]+d and (ll[i][4]>=ll[i][0]-d or (ll[i][4]<ll[i][0]-d and ll[i][5]<ll[i][3])):
        j=ll[i][1]
        l[j],l[j-1]=l[j-1],l[j]
        l[j][1]-=1
        l[j-1][1]+=1
        j-=1
        while j>0 :
            if l[j]>=l[j-1] and l[j]<=l[j+1]:
                break
            else:
                l[j],l[j-1]=l[j-1],l[j]
                j-=1
    else:
        j=ll[i][1]
        if ll[i][1]==0 and abs(l[j]-l[j+1])<=d:
            l[j],l[j+1]=l[j+1],l[j]
            j+=1
            print(' '.join(map(str,l)))
        while j<n-1 :
            if abs(l[j]-l[j+1])>d or (l[j]>=l[j-1] and l[j]<=l[j+1]):
                break
            else:
                l[j],l[j+1]=l[j+1],l[j]
                j+=1
            print(' '.join(map(str,l)))
    print(' '.join(map(str,l)))
