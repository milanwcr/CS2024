p=int(input())
l=[int(s) for s in input().split()]
l.sort()
ans=0
lp,rp=0,len(l)-1
while lp<=rp:
    if p>=l[lp]:
        ans+=1
        p-=l[lp]
        lp+=1
    elif p+l[rp]>=l[lp] and ans!=0:
        p=p+l[rp]-l[lp]
        lp+=1
        rp-=1
    else:
        break
print(ans)