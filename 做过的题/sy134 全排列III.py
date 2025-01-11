def dp(l):
    if len(l)==1:
        return [l]
    store=[]
    same=set()
    for i in range(len(l)):
        if l[i] not in same:
            same.add(l[i])
            lcopy=l[:]
            del lcopy[i]
            next_store=dp(lcopy)
            for j in next_store:
                store.append([l[i]]+j)
    return store

n=int(input())
a=[int(s) for s in input().split()]
a.sort()
ans=dp(a)
for i in ans:
    print(' '.join(map(str,i)))