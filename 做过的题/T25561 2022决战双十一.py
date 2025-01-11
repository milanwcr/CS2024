def find(l):
    global q
    price=sum(l)
    price-=50*(price//300)
    for j in range(m):
        c=0
        for k in q[j]:
            if l[j]>=int(k[:k.index('-')]):
                c=max(c,int(k[k.index('-')+1:]))
        price-=c
    return price

def dfs(l,depth):
    global ans,n,m
    if depth==n:
        ans=min(ans,find(l))
        return
    for i in p[depth]:
        ll=l[:]
        ll[i[0]-1]+=i[1]
        dfs(ll,depth+1)

n,m=map(int,input().split())
p=[[[int(s[0]),int(s[2:])] for s in input().split()] for i in range(n)]
q=[list(input().split()) for i in range(m)]
ans=float('inf')
dfs([0]*m,0)
print(ans)