from collections import Counter
n=int(input())
s=[int(i) for i in input().split()]
c=Counter(s)
ans=c[4]+c[3]
c[1]=max(c[1]-c[3],0)
ans+=c[2]//2+c[2]%2
c[1]=max(c[1]-(c[2]%2)*2,0)
ans+=c[1]//4+(c[1]%4+3)//4
print(ans)